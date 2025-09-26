VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(PYTHON) -m pip
SRC=src
PKG=example

.DEFAULT_GOAL := help

help:
	@echo '사용 가능한 타겟:'
	@grep -E '^[a-zA-Z_-]+:.*?##' Makefile | sed -E 's/:.*?##/\t- /'

bootstrap: ## 가상환경 생성 + 의존성 설치
	@test -d $(VENV) || python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install: ## requirements 재설치 (캐시 무시)
	$(PIP) install --no-cache-dir -r requirements.txt

test: ## pytest 실행
	$(PYTHON) -m pytest -vv

mypy: ## 타입 체크(strict)
	$(PYTHON) -m mypy $(SRC)

lint: ## flake8 린트
	$(VENV)/bin/flake8 $(SRC) tests

ruff: ## ruff 검사
	$(PYTHON) -m ruff check .

fmt: ## black+isort+ruff fix 적용
	$(PYTHON) -m isort $(SRC) tests
	$(PYTHON) -m black $(SRC) tests
	$(PYTHON) -m ruff check --fix $(SRC) tests

clean: ## 캐시/빌드 산출 삭제
	rm -rf .mypy_cache .ruff_cache .pytest_cache
	find $(SRC) tests -name '__pycache__' -type d -prune -exec rm -rf {} +

check: fmt mypy ruff lint test ## 전체 품질 파이프라인

all: check ## 별칭

.PHONY: help bootstrap install test mypy lint ruff fmt clean check all

