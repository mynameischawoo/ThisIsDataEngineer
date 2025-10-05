from enum import Enum

class IcebergMetadataJsonField(Enum):
    FORMAT_VERSION = "format-version"
    TABLE_UUID = "table-uuid"
    LOCATION = "location"
    LAST_SEQUENCE_NUMBER = "last-sequence-number"
    LAST_UPDATED_MS = "last-updated-ms"
    LAST_COLUMN_ID = "last-column-id"
    CURRENT_SCHEMA_ID = "current-schema-id"
    SCHEMAS = "schemas"
    DEFAULT_SPEC_ID = "default-spec-id"
    PARTITION_SPECS = "partition-specs"
    LAST_PARTITION_ID = "last-partition-id"
    DEFAULT_SORT_ORDER_ID = "default-sort-order-id"
    SORT_ORDERS = "sort-orders"
    PROPERTIES = "properties"
    CURRENT_SNAPSHOT_ID = "current-snapshot-id"
    REFS = "refs"
    SNAPSHOTS = "snapshots"
    STATISTICS = "statistics"
    PARTITION_STATISTICS = "partition-statistics"
    SNAPSHOT_LOG = "snapshot-log"
    METADATA_LOG = "metadata-log"


# Enum → 설명 매핑
FIELD_DESCRIPTIONS = {
    IcebergMetadataJsonField.FORMAT_VERSION: "Iceberg 테이블 포맷 버전(https://iceberg.apache.org/spec/)",
    IcebergMetadataJsonField.TABLE_UUID: "테이블을 고유하게 식별하는 UUID(테이블 변경, 데이터 갱신에도 변경되지 않는 정보)",
    IcebergMetadataJsonField.LOCATION: "테이블 데이터와 메타데이터가 저장되는 경로",
    IcebergMetadataJsonField.LAST_SEQUENCE_NUMBER: "마지막으로 커밋된 작업의 시퀀스 번호 (트랜잭션 순서, 테이블 또는 데이터 갱신 작업마다 늘어남)",
    IcebergMetadataJsonField.LAST_UPDATED_MS: "메타데이터가 마지막으로 갱신된 시각 (epoch 밀리초)",
    IcebergMetadataJsonField.LAST_COLUMN_ID: "테이블에서 현재까지 사용된 컬럼 ID 중 가장 큰 값(새로운 컬럼 추가 시 ID를 이어받음)",
    IcebergMetadataJsonField.CURRENT_SCHEMA_ID: "현재 활성화된 스키마의 ID(여러 스키마 중 현재 사용 중인 스키마를 가리킴)",
    IcebergMetadataJsonField.SCHEMAS: "테이블에서 정의된 모든 스키마 리스트(컬럼 구조, 타입, 제약조건 등을 포함함)",
    IcebergMetadataJsonField.DEFAULT_SPEC_ID: "테이블이 기본적으로 사용하는 파티션 규칙(spec)의 ID",
    IcebergMetadataJsonField.PARTITION_SPECS: "파티션 정의 목록",
    IcebergMetadataJsonField.LAST_PARTITION_ID: "파티션 정의에 사용된 마지막 ID 값(새로운 파티션 필드 추가 시 참조됨)",
    IcebergMetadataJsonField.DEFAULT_SORT_ORDER_ID: "테이블의 기본 정렬 규칙(sort order) ID",
    IcebergMetadataJsonField.SORT_ORDERS: "정렬 규칙 정의 목록(특정 컬럼 기준으로 정렬이 필요한 경우 지정)",
    IcebergMetadataJsonField.PROPERTIES: "테이블 속성 (예: 소유자, 압축 코덱 등)",
    IcebergMetadataJsonField.CURRENT_SNAPSHOT_ID: "현재 활성 스냅샷 ID (-1이면 스냅샷 없음)",
    IcebergMetadataJsonField.REFS: "브랜치/태그 같은 참조 정보",
    IcebergMetadataJsonField.SNAPSHOTS: "스냅샷 리스트 (데이터 변경 이력, 테이블이 특정 스냅샷 시점에 어떤 데이터를 가졌는지 기록)",
    IcebergMetadataJsonField.STATISTICS: "테이블 통계 정보 (행 수, null 값 개수 등)",
    IcebergMetadataJsonField.PARTITION_STATISTICS: "파티션 단위 통계 정보(각 파티션별 데이터 분포 확인 가능)",
    IcebergMetadataJsonField.SNAPSHOT_LOG: "스냅샷 변경 이력 로그(언제 어떤 스냅샷이 활성화되었는지 기록)",
    IcebergMetadataJsonField.METADATA_LOG: "메타데이터 파일 변경 이력 로그",
}

# 🔎 사용 예시
if __name__ == "__main__":
    for field in IcebergMetadataJsonField:
        print(f"{field.value}: {FIELD_DESCRIPTIONS[field]}")
