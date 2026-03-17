from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_sales_service
from app.api.presenters import to_monthly_sales_read
from app.schemas.sales import MonthlySalesRead
from app.services.sales_interfaces import SalesService

router = APIRouter(prefix="/sales", tags=["sales"])


@router.get("/monthly", response_model=list[MonthlySalesRead])
def get_monthly_sales(
    brand: str = Query(..., min_length=1),
    category: str = Query(..., min_length=1),
    region: str = Query(..., min_length=1),
    year: int | None = Query(None, ge=2000, le=2100),
    service: SalesService = Depends(get_sales_service),
):
    try:
        items = service.list_monthly_sales_by_name(brand, category, region, year)
        return to_monthly_sales_read(items)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch sales data",
        ) from exc
