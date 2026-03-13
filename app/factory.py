from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.database import engine
from app.models.base import Base
from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact
from app.models.segment import Segment
from app.models.sku import Sku
from app.models.subcategory import Subcategory


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.include_router(api_router)

    @app.on_event("startup")
    def on_startup() -> None:
        Base.metadata.create_all(bind=engine)

    return app
