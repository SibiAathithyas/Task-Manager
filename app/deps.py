from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt
from .database import SessionLocal
from . import crud

SECRET_KEY = "secretkey"
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = crud.get_user(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user