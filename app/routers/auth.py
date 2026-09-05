from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.TokenResponse, responses={401: {"model": schemas.ErrorResponse}})
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    """Validate demo credentials and return a fixed, non-production bearer token."""
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or user.password != data.password:
        raise HTTPException(401, "Invalid email or password")
    return {"access_token": "test-token", "token_type": "bearer"}
