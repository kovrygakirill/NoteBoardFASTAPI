FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip==21.3.1

RUN apt-get update

COPY requirements.txt ./

RUN pip install -r requirements.txt --no-cache-dir

ADD . /home/app
WORKDIR /home/app
