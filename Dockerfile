FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1

COPY . /code
WORKDIR /code

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000


