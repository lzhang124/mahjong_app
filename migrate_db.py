from pathlib import Path

from api.db.db import db_conn


CREATE_VERSION_TABLE = '''
    CREATE TABLE IF NOT EXISTS version (
        id serial PRIMARY KEY,
        version integer
    );
'''


UPSERT_VERSION_ROW = '''
    INSERT INTO version (id, version)
    VALUES (1, 0)
    ON CONFLICT DO NOTHING;
'''


GET_CURRENT_VERSION = '''
    SELECT version FROM version;
'''


UPDATE_VERSION = '''
    UPDATE version
    SET version = %(version)s;
'''


if __name__ == '__main__':
    conn = db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_VERSION_TABLE)
            cur.execute(UPSERT_VERSION_ROW)

    with conn:
        with conn.cursor() as cur:
            cur.execute(GET_CURRENT_VERSION)
            current_version = cur.fetchone()[0]

    versions = [p for p in Path('./api/db/versions').glob('*.sql')]
    max_version = int(max(versions, key=lambda p: int(p.stem)).stem)

    for v in range(current_version + 1, max_version + 1):
        with open(Path('./api/db/versions') / f'{v}.sql', 'r') as f:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f.read())
                    cur.execute(UPDATE_VERSION, {'version': v})

    conn.close()
