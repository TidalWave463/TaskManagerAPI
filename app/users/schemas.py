from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)
from datetime import datetime
from .models import utc_now_native


class Registr(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )
    username: str = Field(

        min_length=1
    )
    
    password: str  = Field(
        default=None,
        max_length=2000
    )


class RegistrResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )
    
    id: int
    username: str
    password: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)