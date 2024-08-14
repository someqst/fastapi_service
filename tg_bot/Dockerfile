FROM python:3.11.1

RUN python -m pip install --upgrade pip

WORKDIR /tgbot

COPY . /tgbot

RUN python3 -m pip install aiogram pydantic pydantic-settings