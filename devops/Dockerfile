#FROM python:3.8-alpine
FROM python:3.8-slim

# RUN apk add --update \
#     curl \
#     bash \
#     && rm -rf /var/cache/apk/*

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    curl \
    bash \
    unzip \
    gcc && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/graphox
WORKDIR /opt

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY graphox/ /opt/graphox/
COPY tests/ /opt/tests/

# only if you dont want to mount datasource folder - docker-compose
#COPY datasource/ /opt/datasource/

COPY devops/run.sh /opt/
RUN chmod +x run.sh

RUN echo 'root:x:0:0:root:/root:/bin/bash\n' >>/etc/passwd

ENTRYPOINT [ "bash","run.sh" ]
