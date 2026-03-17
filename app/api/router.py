from fastapi import APIRouter

from app.api.routes import business_kpi, health, sales

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(sales.router)
api_router.include_router(business_kpi.router)
