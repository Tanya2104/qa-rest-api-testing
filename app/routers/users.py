from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=schemas.UserResponse, status_code=201, summary="Create a user", responses={409: {"model": schemas.ErrorResponse}})
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a customer. Email addresses must be unique."""
    if db.query(models.User).filter(models.User.email == data.email).first():
        raise HTTPException(409, "Email already exists")
    user = models.User(**data.model_dump())
    db.add(user); db.commit(); db.refresh(user)
    return user


@router.get("", response_model=list[schemas.UserResponse], summary="List users")
def list_users(db: Session = Depends(get_db)):
    """Return every registered customer without passwords."""
    return db.query(models.User).all()


@router.get("/{user_id}", response_model=schemas.UserResponse, responses={404: {"model": schemas.ErrorResponse}})
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Return one customer by numeric ID."""
    user = db.get(models.User, user_id)
    if not user: raise HTTPException(404, "User not found")
    return user


@router.put("/{user_id}", response_model=schemas.UserResponse, responses={404: {"model": schemas.ErrorResponse}, 409: {"model": schemas.ErrorResponse}})
def update_user(user_id: int, data: schemas.UserUpdate, db: Session = Depends(get_db)):
    """Replace all editable customer fields."""
    user = db.get(models.User, user_id)
    if not user: raise HTTPException(404, "User not found")
    duplicate = db.query(models.User).filter(models.User.email == data.email, models.User.id != user_id).first()
    if duplicate: raise HTTPException(409, "Email already exists")
    for key, value in data.model_dump().items(): setattr(user, key, value)
    db.commit(); db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=204, responses={404: {"model": schemas.ErrorResponse}})
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Permanently delete a customer."""
    user = db.get(models.User, user_id)
    if not user: raise HTTPException(404, "User not found")
    db.delete(user); db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
