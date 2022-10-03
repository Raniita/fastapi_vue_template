from lib2to3.pytree import Base
from typing import Optional

from pydantic import BaseModel

class TokenData(BaseModel):
    username: Optional[str] = None

class Status(BaseModel):
    message: str