#
# Dockerfile for installing opcua server simulator on IOx enabled platforms
#

# ARM or x86
#FROM arm64v8/python:3.6-alpine
#FROM arm64v8/alpine:3.6
#FROM arm64v8/python:3.6-slim
#FROM arm64v8/python:alpine
#RUN apk add --no-cache python3 
FROM python:3.7
RUN apt-get update && apt-get install build-essential -y
RUN apt-get update && apt-get install pip -y
#RUN apt-get install qemu-user qemu-user-static
#RUN apk add --update build-essential

# RUN apk add --update \
#  py3-pip \
#  gcc \
#  libxml2-dev \
#  libxslt-dev \
#  python-dev \
#  #gcc-multilib \
#  libffi \
#  libffi-dev \
#  gfortran 

#FROM python:3-alpine

# RUN apk add --update \
#  python3
# RUN apk add --update \
#  py3-pip \
#  gcc

#RUN apt-get update && apt-get install -y gcc
#RUN python3 -m pip install --upgrade pip
# COPY qemu-aarch64-static /usr/bin
# COPY requirements.txt etc/requirements.txt
# RUN python3 -m pip install -r etc/requirements.txt

COPY requirements.txt etc/requirements.txt
RUN python3 -m pip install -r etc/requirements.txt

#EXPOSE 4840
EXPOSE 48405
COPY opc-ua-server.py /opc-ua-server.py
COPY sensor.csv /
#COPY main.py /main.py
# LABEL cisco.info.name="opcua" \
#       cisco.info.description="Basic opcua server simulator for IOx" \
#       cisco.info.version="1.6" \
#       cisco.info.author-link="" \
#       cisco.info.author-name="omarine" \
#       cisco.type=docker \
#       cisco.cpuarch=aarch64 \
#       cisco.resources.profile=custom \
#       cisco.resources.cpu=400 \
#       cisco.resources.memory=100 \
#       cisco.resources.disk=100 \
#       cisco.resources.network.0.interface-name=eth0 \
#       cisco.resources.network.0.ports.tcp=[4840]

CMD python3 /opc-ua-server.py
#CMD python3 /main.py
#CMD ["/usr/local/bin/python", "/server-minimal.py"]
#CMD ["/usr/local/bin/python", "/main.py"]