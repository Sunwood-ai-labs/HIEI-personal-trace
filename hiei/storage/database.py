"""Database operations for activity storage."""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from ..utils.logging import get_logger

logger = get_logger(__name__)
Base = declarative_base()

class ActivityRecord(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    activity_type = Column(String(50))  # 'keystroke' or 'clipboard'
    content = Column(Text, nullable=True)
    metadata = Column(Text, nullable=True)  # JSON-encoded metadata

class ActivityDatabase:
    def __init__(self, db_path: str = 'sqlite:///activities.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def store_activity(self, activity_type: str, content: str = None, metadata: dict = None):
        """Store an activity record."""
        try:
            session = self.Session()
            record = ActivityRecord(
                activity_type=activity_type,
                content=content,
                metadata=str(metadata) if metadata else None
            )
            session.add(record)
            session.commit()
        except Exception as e:
            logger.error(f"Error storing activity: {e}")
            session.rollback()
        finally:
            session.close()

    def get_recent_activities(self, limit: int = 100):
        """Get recent activity records."""
        session = self.Session()
        try:
            return session.query(ActivityRecord)\
                .order_by(ActivityRecord.timestamp.desc())\
                .limit(limit)\
                .all()
        finally:
            session.close()
