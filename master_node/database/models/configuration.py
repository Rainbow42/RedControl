import uuid as uuid
import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from database.db.base_class import Base


class Configuration(Base):
    __tablename__ = "configuration"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )
    name = Column(String(255), nullable=False)
    version = Column(
        String(255), nullable=False
    )
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
