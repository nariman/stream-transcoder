FROM python:alpine

WORKDIR /

RUN apt update

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code
RUN pip install -r requirements.txt

ADD . /code

CMD ["python", "server.py"]
