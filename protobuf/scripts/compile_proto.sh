#!/usr/bin/env bash
set -euo pipefail
# Proto 파일을 Python 코드로 생성
# 실행 위치: protobuf 디렉토리 (프로젝트 루트 아님)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
PROTO_DIR="${ROOT_DIR}/proto"
OUT_DIR="${ROOT_DIR}/generated"

mkdir -p "${OUT_DIR}"

echo "[INFO] protoc compile (python + grpc)"
python -m grpc_tools.protoc \
  -I "${PROTO_DIR}" \
  --python_out="${OUT_DIR}" \
  --grpc_python_out="${OUT_DIR}" \
  ${PROTO_DIR}/person/v1/person.proto \
  ${PROTO_DIR}/person/v1/person_service.proto

# mypy-protobuf 플러그인(stub) 생성 (선택)
if command -v protoc-gen-mypy >/dev/null 2>&1; then
  echo "[INFO] generating mypy stubs"
  python -m grpc_tools.protoc \
    -I "${PROTO_DIR}" \
    --mypy_out="${OUT_DIR}" \
    ${PROTO_DIR}/person/v1/person.proto \
    ${PROTO_DIR}/person/v1/person_service.proto || true
else
  echo "[INFO] protoc-gen-mypy 미설치 → 타입 stub 생략" >&2
fi

# 패키지 import 용 __init__.py 보장
for d in "${OUT_DIR}" "${OUT_DIR}/person" "${OUT_DIR}/person/v1"; do
  [ -d "$d" ] || continue
  if [ ! -f "$d/__init__.py" ]; then
    echo "# auto generated" > "$d/__init__.py"
  fi
done

echo "[DONE] generated => ${OUT_DIR}"
