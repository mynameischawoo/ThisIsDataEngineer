# Python 품질 도구 스터디

이 디렉토리는 기본 예제 코드를 대상으로 아래 항목을 한 번에 학습/실행할 수 있는 환경을 제공합니다.

1. Unit Test (pytest)
2. Type Check (mypy)
3. Lint (flake8 + Ruff)
4. Style / Format (black, isort)
5. 통합 실행 Makefile

## 디렉토리 구조
```
python/
  requirements.txt        # 의존성 (품질 도구 포함)
  Makefile                # 실행 명령 집약
  src/example/            # 예제 코드
  tests/                  # 테스트 코드
  mypy.ini                # mypy 설정
  ruff.toml               # ruff 설정
  .flake8                 # flake8 설정
  pytest.ini              # pytest 설정 (src import 용)
```

## 빠른 시작
### 1) 가상환경 & 의존성 설치
```bash
cd python
make bootstrap   # 또는 아래 수동으로
# python -m venv .venv
# . .venv/bin/activate
# pip install -r requirements.txt
```

### 2) 전체 품질 체크 일괄 실행
```bash
make all
```

### 3) 개별 명령
| 목적 | 명령 |
|------|------|
| 테스트 실행 | `make test` |
| 타입 검사 | `make mypy` |
| 린트 (flake8) | `make lint` |
| Ruff 검사 | `make ruff` |
| 자동 포매팅 (black+isort+ruff fix) | `make fmt` |
| 정리(캐시 삭제) | `make clean` |

## Make 타겟 설명
- bootstrap: 가상환경(.venv) 생성 후 의존성 설치
- install: 의존성 재설치(pip)
- test: pytest 실행 (조용 모드 `-q` 아님, 상세 보고 원하면 수정)
- mypy: `src/` 대상 엄격 검사
- lint: flake8 검사 (Ruff 와 함께 중복 일부 있지만 비교용)
- ruff: Ruff 규칙 기반 정적 분석
- fmt: black, isort 후 Ruff 자동 수정(`--fix`)
- check: fmt + mypy + ruff + lint + test (CI 비슷한 합성)
- all: check 별칭

## 도구 설정 개요
- mypy: strict 모드, test 디렉토리 제외 (필요 시 포함)
- black: 기본 line-length 88
- isort: black 호환 프로파일
- flake8: line-length 88, E203 W503 무시 (black 권장 세트)
- ruff: flake8 대체 + 추가 규칙 (반복 학습용 flake8 병행 가능)

## 확장 연습 아이디어
1. example/math_ops.py 에 새 함수 추가 후 TDD 사이클 적용
2. Stats 에 median 함수 추가 후 mypy 통과시키기
3. 의도적 타입 오류 삽입 → mypy 출력 형식 분석
4. ruff 규칙 강화 (e.g. `select = ["E", "F", "I", "N", "UP", "B"]`) 후 위반 수정
5. pre-commit 훅 도입 (선택)

## 트러블슈팅
| 증상 | 원인/해결 |
|------|-----------|
| tests 에서 `ModuleNotFoundError: example` | `pytest.ini` 의 pythonpath 설정 누락 / 작업 디렉토리 확인 |
| mypy 가 test 폴더 미검사 | `mypy.ini` exclude 설정 때문 (제거 후 재실행) |
| ruff 와 flake8 경고 중복 | 점진적 이전 학습 목적. 하나만 쓰고 싶으면 flake8 제거 |

## 참고
- pytest: https://docs.pytest.org/
- mypy: https://mypy.readthedocs.io/
- black: https://black.readthedocs.io/
- isort: https://pycqa.github.io/isort/
- ruff: https://docs.astral.sh/ruff/

즐겁게 품질 도구 파이프라인을 실습해보세요.

