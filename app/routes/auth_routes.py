from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, auth
from ..deps import get_db

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user(db, user.username):
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = crud.create_user(db, user.username, user.password)

    return {
        "id": new_user.id,
        "username": new_user.username
    }

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.username)

    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_access_token({"sub": db_user.username})

    return {"access_token": token, "token_type": "bearer"}