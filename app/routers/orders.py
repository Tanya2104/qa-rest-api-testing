from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("", response_model=schemas.OrderResponse, status_code=201, responses={400: {"model": schemas.ErrorResponse}, 404: {"model": schemas.ErrorResponse}})
def create_order(data: schemas.OrderCreate, db: Session = Depends(get_db)):
    """Create an order, calculate its total, and atomically reduce inventory."""
    if not db.get(models.User, data.user_id): raise HTTPException(404, "User not found")
    product = db.get(models.Product, data.product_id)
    if not product: raise HTTPException(404, "Product not found")
    if data.quantity > product.stock: raise HTTPException(400, "Insufficient stock")
    order = models.Order(**data.model_dump(), total_price=round(product.price * data.quantity, 2), status="created")
    product.stock -= data.quantity
    db.add(order); db.commit(); db.refresh(order); return order

@router.get("", response_model=list[schemas.OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    """List all orders."""
    return db.query(models.Order).all()

@router.get("/{order_id}", response_model=schemas.OrderResponse, responses={404: {"model": schemas.ErrorResponse}})
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Get an order by ID."""
    order = db.get(models.Order, order_id)
    if not order: raise HTTPException(404, "Order not found")
    return order

@router.delete("/{order_id}", status_code=204, responses={404: {"model": schemas.ErrorResponse}})
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """Delete an order. Inventory is not restored (cancellation is out of scope)."""
    order = db.get(models.Order, order_id)
    if not order: raise HTTPException(404, "Order not found")
    db.delete(order); db.commit(); return Response(status_code=status.HTTP_204_NO_CONTENT)
