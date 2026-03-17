from app.domain.business_kpi import BusinessKpi
from app.repositories.business_kpi_interfaces import BusinessKpiRepository
from app.services.business_kpi_interfaces import BusinessKpiService


class DefaultBusinessKpiService(BusinessKpiService):
    def __init__(self, repo: BusinessKpiRepository) -> None:
        self.repo = repo

    def list_business_kpi(
        self,
        year: int,
        month: int,
        brand: str,
        category: str,
    ) -> list[BusinessKpi]:
        return self.repo.list_business_kpi(year, month, brand, category)
