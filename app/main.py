from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, orders, products, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QA Portfolio Shop API",
    version="1.0.0",
    description="A documented training store API for functional, negative, and database testing.",
    contact={"name": "QA Portfolio"},
)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(auth.router)

@app.get("/", tags=["Health"], summary="API health check")
def health():
    """Confirm that the service is available."""
    return {"status": "ok"}
