FROM python:3-slim
# FROM vimagick/python:3
# FROM elyase/pyrun:3.4
# FROM frolvlad/alpine-python3
ENV PYTHONUNBUFFERED=0

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . /app

CMD python3 app.py
