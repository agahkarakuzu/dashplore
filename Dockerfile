FROM python:3.6

USER root

WORKDIR /app

ADD . /app/requirements.txt
ADD . /app/app.py

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8050

USER 1001
