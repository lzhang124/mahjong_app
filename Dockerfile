FROM python:3.7.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn -w 1 -b 0.0.0.0:8080 --timeout 0 flask_app:app
