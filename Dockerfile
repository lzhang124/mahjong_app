FROM python:3.7.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app
