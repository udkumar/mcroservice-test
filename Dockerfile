FROM python:3.9.5-slim-buster

RUN mkdir usr/src/IKEA
WORKDIR usr/src/IKEA

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# CMD ["gunicorn", "app", "--host", "0.0.0.0", "--port", "8000"]