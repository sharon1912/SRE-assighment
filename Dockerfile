
FROM ubuntu:latest

WORKDIR /tmp

ENV VERSION=1.2.0

RUN apt-get update && \
    apt-get install -y python3 vim zip unzip && \
    apt-get clean 

COPY ./zip_job.py /tmp

CMD cat /etc/os-release; cat /tmp/zip_job.py
