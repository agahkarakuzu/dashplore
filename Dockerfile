FROM python:3.6.2

RUN mkdir -p /home/project/dash_app
WORKDIR /home/project/dash_app
ADD ./requirements.txt /home/project/dash_app/requirements.txt
ADD ./app.py /home/project/dash_app/app.py

RUN pip install --no-cache-dir -r /home/project/dash_app/requirements.txt

EXPOSE 8050
