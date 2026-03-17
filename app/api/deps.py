from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.business_kpi import SqlAlchemyBusinessKpiRepository
from app.repositories.business_kpi_interfaces import BusinessKpiRepository
from app.repositories.sales import SqlAlchemySalesRepository
from app.repositories.sales_interfaces import SalesRepository
from app.services.business_kpi import DefaultBusinessKpiService
from app.services.business_kpi_interfaces import BusinessKpiService
from app.services.sales import DefaultSalesService
from app.services.sales_interfaces import SalesService


def get_sales_repository(db: Session = Depends(get_db)) -> SalesRepository:
    return SqlAlchemySalesRepository(db)


def get_sales_service(repo: SalesRepository = Depends(get_sales_repository)) -> SalesService:
    return DefaultSalesService(repo)


def get_business_kpi_repository(db: Session = Depends(get_db)) -> BusinessKpiRepository:
    return SqlAlchemyBusinessKpiRepository(db)


def get_business_kpi_service(
    repo: BusinessKpiRepository = Depends(get_business_kpi_repository),
) -> BusinessKpiService:
    return DefaultBusinessKpiService(repo)
