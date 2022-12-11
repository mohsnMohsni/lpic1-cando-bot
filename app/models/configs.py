# Third-party imports.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_FILE = 'default.sqlite3'


default_engine = create_engine('sqlite:///%s' % DB_FILE, echo=True)
default_session = sessionmaker(bind=default_engine)


def apply_migration(schema) -> None:
    schema.metadata.create_all(default_engine)
