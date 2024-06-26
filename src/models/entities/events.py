from sqlalchemy import Column, Integer, String

from src.models.settings.base import Base


class Events(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return f"Events [title={self.title}, slug={self.slug}]"
