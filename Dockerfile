# syntax=docker/dockerfile:1

FROM python:3.10.7

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=printer_business.settings
ENV PYTHONPATH=/app
RUN python3 manage.py migrate

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
