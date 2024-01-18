from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

class Response(BaseModel):
    message: Optional[str]
    jwt: Optional[str]
    email: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]