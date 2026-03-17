from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_business_kpi_service
from app.api.presenters import to_business_kpi_read
from app.schemas.business_kpi import BusinessKpiRead
from app.services.business_kpi_interfaces import BusinessKpiService

router = APIRouter(prefix="/business-kpi", tags=["business-kpi"])


@router.get("/", response_model=list[BusinessKpiRead])
def get_business_kpi(
    year: int = Query(..., ge=2000, le=2100),
    month: int = Query(..., ge=1, le=12),
    brand: str = Query(..., min_length=1),
    category: str = Query(..., min_length=1),
    service: BusinessKpiService = Depends(get_business_kpi_service),
):
    try:
        items = service.list_business_kpi(year, month, brand, category)
        return to_business_kpi_read(items)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch business KPI data",
        ) from exc
