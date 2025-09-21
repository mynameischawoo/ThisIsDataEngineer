# PR 제목
예시: ✨ feat: Iceberg 테이블 스키마 변경 처리
> 제목 규칙: [gitmoji] type: 간결한 설명 (영문/국문 택1). 예: 🐛 fix: MinIO 연결 재시도 로직 수정

## 관련 이슈
Resolves #번호 / Closes #번호 / Ref #번호

## 변경 유형 (Change Type)
- [ ] ✨ feat: 새로운 기능 추가
- [ ] 🐛 fix: 버그 수정
- [ ] ♻️ refactor: 리팩터링 (동작 변경 없음)
- [ ] 📝 docs: 문서만 변경
- [ ] ✅ test: 테스트 추가/개선
- [ ] 🎨 style: 포맷/스타일 (세미콜론, 들여쓰기 등)
- [ ] 🚀 perf: 성능 개선
- [ ] 🧹 chore: 빌드/도구/환경 설정
- [ ] 🔧 config: 설정 파일 변경
- [ ] ⏪ revert: 변경 되돌리기
- [ ] ⚠️ breaking change: 호환성 깨짐

## 변경 요약
- 핵심 변경사항 2~5줄 bullet
- ...

## 상세 내용
필요 시 설명, 설계 배경, 선택지 비교 등.

## 스크린샷 / 로그 (선택)
| 구분 | 내용 |
|------|------|
| Before | 첨부 |
| After  | 첨부 |

```
필요한 로그/쿼리/커맨드
```

## 테스트
- [ ] 로컬에서 기본 시나리오 동작 확인
- [ ] docker-compose 환경(iceberg)에서 수동 검증
- [ ] 관련 Notebook 영향 검토
- [ ] 문서(README / 예제) 업데이트

## 체크리스트
- [ ] 커밋 메시지 규칙(gitmoji + 타입 + 설명) 준수
- [ ] 불필요한 파일/디버그 출력 제거
- [ ] .gitignore에 포함되어야 할 산출물 없음
- [ ] 리뷰어가 재현 가능한 절차 명시
- [ ] Breaking Change 여부 표시
- [ ] 필요한 경우 마이그레이션/롤백 방법 기술

## 추가 고려 / 후속 작업 (선택)
- [ ] 후속: 

## 참고 (References)
- Issue / Spec / Docs 링크

---
### gitmoji 참고 (일부)
| 이모지 | 의미 | 예시 prefix |
|--------|------|-------------|
| ✨ | 기능 추가 | feat |
| 🐛 | 버그 수정 | fix |
| ♻️ | 리팩터링 | refactor |
| 📝 | 문서 | docs |
| ✅ | 테스트 | test |
| 🚀 | 성능 | perf |
| 🎨 | 스타일 | style |
| 🔧 | 설정 | config |
| 🧹 | 기타 정리 | chore |
| ⏪ | 되돌리기 | revert |
| ⚠️ | Breaking | breaking |

불필요한 섹션은 삭제하거나 간략화해도 됩니다.
