import os
import pathlib
import subprocess
import time
from concurrent import futures

import grpc

# 1. 필요 시 proto 컴파일
ROOT = pathlib.Path(__file__).resolve().parents[1]
GENERATED_FLAG = ROOT / "generated" / "person" / "v1" / "person_pb2.py"
if not GENERATED_FLAG.exists():
    subprocess.check_call(["bash", "scripts/compile_proto.sh"], cwd=ROOT)

# 2. 모듈 import (생성 후 가능)
from generated.person.v1 import person_pb2, person_service_pb2, person_service_pb2_grpc  # type: ignore
import server  # PersonService 클래스 재사용


def _start_test_server(port: int = 50052):
    srv = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    person_service_pb2_grpc.add_PersonServiceServicer_to_server(server.PersonService(), srv)
    srv.add_insecure_port(f"localhost:{port}")
    srv.start()
    return srv


def test_person_crud_and_streaming():
    port = 50052
    srv = _start_test_server(port)
    try:
        channel = grpc.insecure_channel(f"localhost:{port}")
        stub = person_service_pb2_grpc.PersonServiceStub(channel)

        # Create
        created = stub.CreatePerson(
            person_service_pb2.CreatePersonRequest(
                person=person_pb2.Person(id=101, name="Tester", gender=person_pb2.Gender.MALE)
            )
        )
        assert created.id == 101
        assert created.name == "Tester"
        assert created.created_at.seconds > 0  # 서버에서 timestamp 채움

        # Get
        got = stub.GetPerson(person_service_pb2.GetPersonRequest(id=101))
        assert got.id == 101

        # List (server streaming)
        listed_ids = [p.id for p in stub.ListPersons(person_service_pb2.ListPersonsRequest(page_size=10))]
        assert 101 in listed_ids

        # Chat (bidirectional streaming) - echo 형태
        def gen():
            for i in range(102, 105):
                yield person_pb2.Person(id=i, name=f"User{i}")

        echoed = list(stub.Chat(gen()))
        assert {e.id for e in echoed} == {102, 103, 104}
        for e in echoed:
            assert e.created_at.seconds > 0

        # StreamPersons 제한된 메시지 (max_messages=2)
        stream_iter = stub.StreamPersons(person_service_pb2.StreamPersonsRequest(interval_seconds=1, max_messages=2))
        received = list(stream_iter)
        assert len(received) == 2
    finally:
        srv.stop(0)

