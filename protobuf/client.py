import grpc
from google.protobuf import empty_pb2
from google.protobuf import timestamp_pb2

from generated.person.v1 import person_pb2, person_service_pb2, person_service_pb2_grpc


def build_person(person_id: int, name: str, gender: person_pb2.Gender = person_pb2.Gender.GENDER_UNSPECIFIED) -> person_pb2.Person:
    return person_pb2.Person(id=person_id, name=name, gender=gender)


def run(host: str = "localhost", port: int = 50051):
    channel = grpc.insecure_channel(f"{host}:{port}")
    stub = person_service_pb2_grpc.PersonServiceStub(channel)

    print("[CLIENT] CreatePerson ...")
    p = build_person(1, "Alice", person_pb2.Gender.FEMALE)
    created = stub.CreatePerson(person_service_pb2.CreatePersonRequest(person=p))
    print("Created:", created)

    print("[CLIENT] GetPerson ...")
    got = stub.GetPerson(person_service_pb2.GetPersonRequest(id=1))
    print("Got:", got)

    print("[CLIENT] ListPersons ...")
    for item in stub.ListPersons(person_service_pb2.ListPersonsRequest(page_size=5)):
        print("List item:", item.id, item.name)

    print("[CLIENT] StreamPersons (first 3) ...")
    stream_iter = stub.StreamPersons(person_service_pb2.StreamPersonsRequest(interval_seconds=1, max_messages=3))
    for s in stream_iter:
        print("Stream:", s.id, s.name)

    print("[CLIENT] Bidirectional Chat (send 3 persons) ...")
    def gen():
        for i in range(2, 5):
            yield build_person(i, f"User{i}")

    for echo in stub.Chat(gen()):
        print("Chat echo:", echo.id, echo.name, echo.created_at.seconds)


if __name__ == "__main__":
    run()

