# Protobuf / gRPC Python 스터디 가이드

이 디렉토리는 Python 기반으로 Protocol Buffers(이하 Protobuf) 와 gRPC 를 학습/실습하기 위한 최소 예제를 제공합니다.

## 1. 디렉토리 구조
```
protobuf/
  proto/                       # .proto 원본 (버전 디렉토리 포함: person/v1)
    person/v1/person.proto
    person/v1/person_service.proto
  generated/                   # (생성) protoc 컴파일 산출물 - Git에 커밋하지 않는 것을 권장
  scripts/
    compile_proto.sh           # 코드 생성 스크립트
  server.py                    # gRPC 서버 구현 예시
  client.py                    # gRPC 클라이언트 사용 예시
  requirements.txt             # 학습용 의존성 고정
  tests/
    test_person_service.py     # 간단 통합 테스트
```

## 2. 빠른 시작
### (1) 의존성 설치
```bash
cd protobuf
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### (2) 코드 생성 (protoc 실행)
```bash
bash scripts/compile_proto.sh
```
- `generated/` 하위에 `person_pb2.py`, `person_service_pb2.py`, `*_grpc.py` 등이 만들어집니다.
- 생성물은 재생성 가능하므로 일반적으로 버전관리 제외(.gitignore)에 두는 것을 권장.

### (3) 서버 실행
```bash
python server.py
```
로그 예: `[gRPC] PersonService started on 0.0.0.0:50051`

### (4) 클라이언트 실행 (다른 터미널)
```bash
python client.py
```
Create / Get / List / Stream / Chat (양방향 스트리밍) 예시 출력 확인.

### (5) 테스트 실행
```bash
pytest -q
```

## 3. Protobuf 핵심 개념 요약
- schema-first: `.proto` 파일에 메시지(데이터 모델)와 서비스(RPC 인터페이스) 정의
- 타입 안정성 + 바이너리 직렬화 (JSON 대비 작고 빠르게 전송)
- 전방/후방 호환성(backward/forward compatibility) 고려가 가장 중요

### 메시지 정의 규칙 (proto3)
- 모든 필드는 기본값(0, 빈 문자열 등)을 가짐 (presence 구분이 필요한 경우 `optional` 키워드 사용 가능 - proto3 최신)
- 필드 번호(field number)는 1~2^29-1 범위. 1~15 는 1바이트 최적화 → 빈번/핵심 필드에 사용
- `enum` 은 반드시 0 값을 하나 정의 (UNSPECIFIED 등)
- `oneof` 은 상호 배타 필드 → 마지막에 set 한 값만 유지
- `map<key, value>`: 내부적으로 entry 메시지로 확장됨, 순서 비보장
- timestamp/datetime 은 `google.protobuf.Timestamp` 활용 (UTC 사용, 서버/클라이언트 변환 주의)
- 중첩 구조 복잡도 최소화 (읽기/버전 관리 편의)

### 호환성 Best Practice
| 변경 유형 | 안전 여부 | 방법 |
|-----------|-----------|------|
| 새 필드 추가 | 안전(기본값) | 새 번호 부여 (기존 번호/이름 재사용 금지) |
| 필드 제거 | 주의 | 실제 제거 전 `reserved` 로 번호/이름 확보 |
| 필드 타입 변경 | 보통 위험 | 새 필드로 추가 후 단계적으로 이전 |
| 필드 번호 재사용 | 금지 | 절대 하지 말 것 (디코딩 혼란) |
| 패키지/메시지 이름 변경 | 위험 | 새로 정의 + 점진적 마이그레이션 |

예: 제거한 필드에 대해
```proto
message Example {
  // before: string nickname = 4;  // 제거
  reserved 4;          // 번호 재사용 금지 보호
  reserved "nickname"; // 이름 재사용 금지 보호
}
```

### 버저닝 전략
- 패키지 경로에 버전 폴더 (`person.v1`) → API 브레이킹 변경 필요 시 `v2` 추가 후 공존
- 클라이언트가 혼재 접근 가능 → 점진적 이전

### 디렉토리/생성물 전략
- `proto/` : 사람 손으로 유지
- `generated/` : 항상 재생성 (CI 캐시 가능) → 필요 시 `.gitignore` 설정
- 모듈 import 경로 혼란 방지를 위해 생성 후 `__init__.py` 자동 생성

## 4. gRPC 패턴 정리
| 패턴 | 요청 | 응답 | 사용 예 |
|------|------|------|---------|
| Unary | 1 | 1 | 단건 조회/생성 |
| Server Streaming | 1 | N | 리스트, 구독 비슷 |
| Client Streaming | N | 1 | 대량 업로드 후 단일 응답 |
| Bidirectional Streaming | N | N | 채팅, 실시간 동기화 |

본 예제: `GetPerson`(Unary), `ListPersons`/`StreamPersons`(서버 스트리밍), `Chat`(양방향).

## 5. 학습 과제 (연습 아이디어)
1. Person 에 `optional string nickname = 11;` 필드 추가 → 클라이언트/서버 코드 수정 없이 동작 관찰
2. `mobile` / `telephone` oneof 중 `telephone` 을 제거 → 즉시 삭제 대신 `reserved` 로 바꿔보기
3. 서버에 단순 캐시 만료 로직 추가 (생성 후 60초 지나면 ListPersons 에서 제외)
4. `ListPersonsRequest` 에 `filter_name_prefix` 필드 추가해 서버 필터 구현
5. Bidirectional Chat 에 클라이언트가 5명 전송 시 서버가 id 누적 합계를 주기적으로 별도 메시지로 내려보내는 형태로 확장
6. mypy 타입 검사 실행: `mypy server.py` (mypy-protobuf 설치/생성 필요)
7. 성능 프로파일: 1만 Person 생성 후 직렬화/역직렬화 속도 측정 (pickle 대비)

## 6. 코드 생성/타입 활용 Tips
- `grpc_tools.protoc` 사용 시 시스템 `protoc` 미설치라도 동작 (내장)
- 타입 힌트 강화 원하면 `mypy-protobuf` 플러그인 사용 (`--mypy_out`)
- Generated 코드 직접 수정 금지 → 항상 .proto 변경 후 재생성
- Python import 문제 발생 시 `sys.path` / 패키지 루트 정렬 (여기선 `generated/` 에 `__init__.py` 넣어 해결)

## 7. 에러 처리 / 상태 코드
- gRPC 예외: `context.abort(StatusCode.NOT_FOUND, "message")`
- 공통 StatusCode: `INVALID_ARGUMENT`, `ALREADY_EXISTS`, `NOT_FOUND`, `PERMISSION_DENIED`, `DEADLINE_EXCEEDED` 등
- 클라이언트에서 try/except `grpc.RpcError` 로 status code 및 details 확인

## 8. 테스트 전략
- 단순 통합: in-process 서버 띄워 Stub 호출
- streaming 은 일정 개수만 소비하여 테스트 시간 단축
- 회귀검증: 새 필드 추가 후 기존 테스트 통과 여부로 호환성 확인

## 9. 유용한 명령 모음
```bash
# 코드 스타일
black . && isort .

# 타입 검사 (mypy-protobuf stub 생성 후)
mypy server.py

# 재생성 전체 수행
bash scripts/compile_proto.sh
```

## 10. 참고 자료
- 공식: https://protobuf.dev/ , https://grpc.io/docs/languages/python/
- Google API Improvement Proposals (AIP) → 필드/메서드 명명 규칙 참고

---
즐겁게 실습하며: 작은 변경(필드 추가/삭제)을 반복 → 재생성 → 테스트 → 구버전 클라이언트 영향 관찰 흐름을 익히세요.
