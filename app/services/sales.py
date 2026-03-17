from app.domain.monthly_sales import MonthlySales
from app.repositories.sales_interfaces import SalesRepository
from app.services.sales_interfaces import SalesService


class DefaultSalesService(SalesService):
    def __init__(self, repo: SalesRepository) -> None:
        self.repo = repo

    def list_monthly_sales_by_name(
        self,
        brand: str,
        category: str,
        region: str,
        year: int | None,
    ) -> list[MonthlySales]:
        return self.repo.list_monthly_sales_by_name(brand, category, region, year)
