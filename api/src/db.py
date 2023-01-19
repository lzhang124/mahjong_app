import logging
from pathlib import Path

from sqlalchemy import create_engine, func, Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from api.config.config import DB_URI


logger = logging.getLogger(__name__)


engine = create_engine(DB_URI)
Session = sessionmaker(engine)


CREATE_VERSION_TABLE = '''
    CREATE TABLE IF NOT EXISTS version (
        id serial PRIMARY KEY,
        version integer
    );

    INSERT INTO version (id, version)
    VALUES (1, 0)
    ON CONFLICT DO NOTHING;
'''


GET_CURRENT_VERSION = '''
    SELECT version
    FROM version;
'''


UPDATE_VERSION = '''
    UPDATE version
    SET version = :version;
'''


def migrate_db():
    with Session() as session:
        session.execute(CREATE_VERSION_TABLE)
        session.commit()

        res = session.execute(GET_CURRENT_VERSION).first()
        current_version = res[0]

        versions = [p for p in Path('./api/src/versions').glob('*.sql')]
        max_version = int(max(versions, key=lambda p: int(p.stem)).stem)

        if max_version > current_version:
            logger.info(f'Migrating db: {current_version} -> {max_version}')

        for v in range(current_version + 1, max_version + 1):
            with open(Path('./api/src/versions') / f'{v}.sql', 'r') as f:
                session.execute(f.read())
                session.execute(UPDATE_VERSION, {'version': v})
                session.commit()


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
