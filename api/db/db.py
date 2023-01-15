import psycopg2

from api.config.config import DB_URI


def db_conn():
    print('DB_URI', DB_URI)
    return psycopg2.connect(DB_URI)
