from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..deps import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_task(db, task.title, task.description, user.id)

@router.get("/", response_model=List[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_tasks(db, user.id)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = crud.get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}/complete", response_model=schemas.TaskOut)
def complete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = crud.get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.mark_completed(db, task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = crud.get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task)