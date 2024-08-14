FROM python:3.11.1

RUN python -m pip install --upgrade pip

WORKDIR /back

COPY . /back

RUN python3 -m pip install fastapi motor pydantic pydantic-settings redis