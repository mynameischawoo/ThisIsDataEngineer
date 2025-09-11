# ThisIsDataEngineer
DataEngineering Study

## Git 설정

### .gitignore 파일 추가하기

`.gitignore` 파일은 Git에서 추적하지 않을 파일이나 폴더를 지정하는 파일입니다.

#### 1. .gitignore 파일 생성
프로젝트 루트 디렉토리에 `.gitignore` 파일을 생성합니다:

```bash
touch .gitignore
```

#### 2. .gitignore 규칙 작성
다음과 같은 패턴을 사용하여 무시할 파일을 지정할 수 있습니다:

- `filename.txt` - 특정 파일 무시
- `*.log` - 특정 확장자를 가진 모든 파일 무시
- `temp/` - 특정 디렉토리와 그 하위 내용 무시
- `!important.log` - 무시 규칙의 예외 지정 (느낌표 사용)

#### 3. 일반적인 .gitignore 항목들

**IDE 관련:**
```
.idea/
.vscode/
*.swp
*.swo
```

**운영체제 관련:**
```
.DS_Store
Thumbs.db
```

**로그 및 임시 파일:**
```
*.log
*.tmp
*.temp
logs/
```

**환경 변수:**
```
.env
.env.local
```

#### 4. 이미 추적 중인 파일 무시하기
이미 Git이 추적하고 있는 파일을 무시하려면:

```bash
git rm --cached filename
git commit -m "Remove file from tracking"
```

#### 5. .gitignore 적용 확인
```bash
git status
```

무시된 파일들이 목록에 나타나지 않으면 정상적으로 적용된 것입니다.
