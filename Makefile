install:
	pip install -U pip && pip install --no-cache-dir -r requirements.txt

migrate:
	python migrate_db.py

run:
	./start_app.sh
