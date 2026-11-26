from ..database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Text, DateTime, String, ForeignKey, UniqueConstraint
from datetime import datetime, timezone

def utc_now_native():
    return datetime.now(timezone.utc).replace(tzinfo=None)

class Task(Base):
    __tablename__ = "auth"
    
    id = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = mapped_column(
            Integer,
            ForeignKey('users.id'),
            nullable=False
        )
    
    token_hash = mapped_column(
        String(64),
        nullable=False,
        unique=True
    )
    
    created_at = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=utc_now_native
    )

    expires_at = mapped_column(
            DateTime(timezone=False),
            nullable=False,
            default=utc_now_native
    )