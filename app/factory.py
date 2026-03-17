from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

import app.models  # noqa: F401
from app.api.router import api_router
from app.core.config import settings
from app.core.database import engine
from app.models.base import Base


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.include_router(api_router)
    return app
