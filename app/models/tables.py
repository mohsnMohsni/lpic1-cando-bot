# Third-party imports.
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

# Local imports with absolute path.
from .configs import apply_migration
from .managers import BaseManager


BaseSchema = declarative_base(name='BaseSchema')


class CapturesVideo(BaseManager, BaseSchema):
    __tablename__ = 'captures_video'

    id = Column(Integer, primary_key=True)
    capture_number = Column(Integer)
    link = Column(String)


apply_migration(BaseSchema)
