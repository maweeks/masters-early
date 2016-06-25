import sys
import os

from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class TimeCount(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    timestamp = Column(DateTime, nullable = False)
    count = Column(Integer, nullable = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'count': self.count,
        }

engine = create_engine('sqlite:///dEarly.db')

Base.metadata.create_all(engine)