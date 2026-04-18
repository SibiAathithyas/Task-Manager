from sqlalchemy.orm import Session
from . import models, auth

def create_user(db: Session, username: str, password: str):
    hashed = auth.hash_password(password)
    user = models.User(username=username, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_task(db: Session, title: str, description: str, user_id: int):
    task = models.Task(title=title, description=description, owner_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()

def mark_completed(db: Session, task):
    task.completed = True
    db.commit()
    return task

def delete_task(db: Session, task):
    db.delete(task)
    db.commit()