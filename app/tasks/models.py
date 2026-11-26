from ..database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Text, DateTime, String, ForeignKey
from datetime import datetime, timezone

def utc_now_native():
    return datetime.now(timezone.utc).replace(tzinfo=None)

class Task(Base):
    __tablename__ = "tasks"
    
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
    
    title = mapped_column(
        String(150),
        nullable=False
    )
    
    description = mapped_column(
        Text,
        nullable=True,
        default=None
    )
    
    status = mapped_column(
        String(20),
        nullable=False,
        default="Pending"
    )

    priority = mapped_column(
            String(10),
            nullable=False,
            default="Medium"
    )
    
    created_at = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=utc_now_native
    )

    updated_at = mapped_column(
            DateTime(timezone=False),
            nullable=False,
            default=utc_now_native
    )