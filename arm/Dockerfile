FROM arm64v8/python:3.7-slim
#FROM python:3.7
#RUN pip3 install bottle

#RUN apt-get update && apt-get install build-essential -y
COPY requirements.txt etc/requirements.txt
RUN python3 -m pip install -r etc/requirements.txt

EXPOSE 48401
#EXPOSE 8000

COPY server-minimal_2.py /server-minimal_2.py


CMD ["/usr/local/bin/python", "/server-minimal_2.py"]
#CMD python3 /server-minimal_2.py

#CMD ["/usr/local/bin/python", "/main.py"]
