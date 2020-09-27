FROM python:3

RUN useradd -ms /bin/bash django && apt-get update && apt-get install python3-dev default-libmysqlclient-dev  -y && pip3 uninstall mysqlclient && pip3 uninstall pymysql &&  pip3 install mysqlclient

USER django

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/app

RUN pip install -r requirements.txt && pip3 install -U mysqlclient

COPY . /home/django

