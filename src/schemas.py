from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    phone_number: str = Field(max_length=12)

class ContactModel(ContactBase):
    email: str = Field(max_length=50)
    birthday: date = Field()

class ContactResponse(ContactBase):
    id: int
    email: str
    birthday: date

    class Config:
            orm_mode = True