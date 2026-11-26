from ..database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, DateTime, String
from datetime import datetime, timezone

def utc_now_native():
    return datetime.now(timezone.utc).replace(tzinfo=None)

class User(Base):
    __tablename__ = "users"
    
    id = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    username = mapped_column(
        String(32),
        nullable=False
    )

    password_hash = mapped_column(
        String(255),
        nullable=False,
    )

    created_at = mapped_column(
        DateTime(timezone=False),
        nullable=False,
        default=utc_now_native
    )
