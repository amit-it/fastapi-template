from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.sales import SqlAlchemySalesRepository
from app.services.sales import SalesService


def get_sales_repository(db: Session = Depends(get_db)) -> SqlAlchemySalesRepository:
    return SqlAlchemySalesRepository(db)


def get_sales_service(repo: SqlAlchemySalesRepository = Depends(get_sales_repository)) -> SalesService:
    return SalesService(repo)
