import logging

import psycopg2

from api.config.config import DB_URI


logger = logging.getLogger(__name__)


def db_conn():
    logger.info(f'DB_URI={DB_URI}')
    return psycopg2.connect(DB_URI)
