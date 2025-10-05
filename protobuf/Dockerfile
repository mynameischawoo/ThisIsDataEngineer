FROM python:3.12.10-slim


WORKDIR /work


RUN apt-get update && \
    apt-get install -y --no-install-recommends protobuf-compiler

# Install python packages
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt


CMD ["python3"]