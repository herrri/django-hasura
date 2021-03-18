FROM python:3.7-alpine as base

FROM base as builder
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
WORKDIR /app
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt
COPY ./django_project /app

FROM base as production
ENV PYTHONUNBUFFERED 1
COPY --from=builder /root/.local /root/.local
RUN apk --no-cache add libpq
COPY ./django_project /app
WORKDIR /app