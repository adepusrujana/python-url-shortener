from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import sessionLocal
from schemas import BaseURL
from models import url
import random
import string



router = APIRouter(prefix="/url", tags=["url"])

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_url():
    return ''.join(random.choices(string.ascii_letters + string.digits,k=6))

@router.post('/shorten')
def shorten_url(data:BaseURL,
                db:Session=Depends(get_db)):
    code = generate_url()
    new_url = url(original_url = data.original_url,
        short_url=code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return {"short_url":f"http://localhost:8000/{code}"}


