FROM python:3.6

USER root

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
ADD ./app.py /app/app.py

RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

EXPOSE 8050

USER 1001
