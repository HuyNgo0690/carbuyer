FROM python:3.9.15-alpine3.16

WORKDIR /app

# Install python packages
RUN python -m pip install --upgrade pip
RUN apk update && apk add gcc libc-dev musl-dev libffi-dev
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app

USER root

EXPOSE 8000
CMD ["python", "main.py"]