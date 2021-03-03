FROM ubuntu:18.04
COPY tp /tp
RUN apt update && apt install -y python3-pip
RUN pip3 install flask
WORKDIR /tp
CMD python3 hello.py
