install:
	pip install --no-cache-dir -r requirements.txt

run:
	gunicorn -w 1 -b 0.0.0.0:8080 --timeout 0 app:app
