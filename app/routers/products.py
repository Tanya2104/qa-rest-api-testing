from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("", response_model=schemas.ProductResponse, status_code=201)
def create_product(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Add a sellable product with its current inventory."""
    item = models.Product(**data.model_dump()); db.add(item); db.commit(); db.refresh(item); return item

@router.get("", response_model=list[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db)):
    """List the product catalog."""
    return db.query(models.Product).all()

@router.get("/{product_id}", response_model=schemas.ProductResponse, responses={404: {"model": schemas.ErrorResponse}})
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get a product by ID."""
    item = db.get(models.Product, product_id)
    if not item: raise HTTPException(404, "Product not found")
    return item

@router.put("/{product_id}", response_model=schemas.ProductResponse, responses={404: {"model": schemas.ErrorResponse}})
def update_product(product_id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Replace product name, price, and inventory."""
    item = db.get(models.Product, product_id)
    if not item: raise HTTPException(404, "Product not found")
    for key, value in data.model_dump().items(): setattr(item, key, value)
    db.commit(); db.refresh(item); return item

@router.delete("/{product_id}", status_code=204, responses={404: {"model": schemas.ErrorResponse}})
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Permanently delete a product."""
    item = db.get(models.Product, product_id)
    if not item: raise HTTPException(404, "Product not found")
    db.delete(item); db.commit(); return Response(status_code=status.HTTP_204_NO_CONTENT)
