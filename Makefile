install.pyenv:
	@if command -v pyenv >/dev/null 2>&1; then \
		echo "✅ 이미 pyenv가 설치되어 있습니다: $$(which pyenv)"; \
		exit 0; \
	else \
		echo "📦 pyenv가 설치되어 있지 않습니다."; \
		brew install pyenv && brew install pyenv-virtualenv; \
		echo 'export PATH="$$HOME/.pyenv/bin:$$PATH"' >> ~/.zshrc; \
		echo 'eval "$$(pyenv init -)"' >> ~/.zshrc; \
		echo 'eval "$$(pyenv virtualenv-init -)"' >> ~/.zshrc; \
		source $$HOME/.zshrc; \
		echo "✅ pyenv 설치가 완료되었습니다: $$(which pyenv)"; \
	fi