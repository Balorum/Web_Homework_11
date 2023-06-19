from typing import List
from datetime import date, datetime
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_days_to_birthday(skip: int, limit: int, db: Session) -> List[Contact]:
    birthday_days = []
    nowdays_date = datetime.now().date()
    days = db.query(Contact).offset(skip).limit(limit).all()
    for i in days:
        birtday_year = date(year=i.birthday.year+(nowdays_date.year-i.birthday.year), month=i.birthday.month, day=i.birthday.day)
        if (birtday_year-nowdays_date).days <=7 and (birtday_year-nowdays_date).days >=0:
            birthday_days.append(i)
    return birthday_days

async def get_by_name(skip: int, limit: int, name: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.name==name).offset(skip).limit(limit).all()

async def get_by_surname(skip: int, limit: int, surname: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.surname==surname).offset(skip).limit(limit).all()

async def get_by_email(skip: int, limit: int, email: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.email==email).offset(skip).limit(limit).all()

async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(name=body.name, surname=body.surname, phone_number=body.phone_number,\
                      email=body.email, birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name=body.name, 
        contact.surname=body.surname, 
        contact.phone_number=body.phone_number,
        contact.email=body.email, 
        contact.birthday=body.birthday
        db.commit()
    return contact
