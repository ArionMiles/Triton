from sqlalchemy import Column, String, Integer
from database import Base


class UniqueID(Base):
    __tablename__ = 'date_added'
    id = Column(Integer, primary_key = True)
    updated_at = Column(String(512))

    def __init__(self, updated_at=None):
        self.updated_at = updated_at

    def __repr__(self):
        return '<Date Added: {}>'.format(self.updated_at)