PROTOBUF_IMAGE_TAG = v1.0.0

docker.build.local:
	docker build \
		--platform linux/amd64 \
		-t python_proto:$(PROTOBUF_IMAGE_TAG) .

docker.run:
	docker run -it --rm \
		--platform linux/amd64 \
		--name python_proto_container \
		-v ${PWD}:/app \
		python_proto:$(PROTOBUF_IMAGE_TAG) \
		bash


pyenv.install.protobuf_env:
	pyenv install 3.12.10
	pyenv virtualenv 3.12.10 protobuf_env

pyenv.activate.local.protobuf_env: 
	pyenv local protobuf_env

pyenv.check.versions:
	pyenv versions

pip.install.requirements:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt


# pyenv virtualenv-delete -f protobuf_env
# pyenv uninstall -f 3.12.10