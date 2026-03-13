from app.repositories.sales import SqlAlchemySalesRepository
from app.schemas.sales import MonthlySalesRead


class SalesService:
    def __init__(self, repo: SqlAlchemySalesRepository) -> None:
        self.repo = repo

    def list_monthly_sales_by_name(
        self,
        brand: str,
        category: str,
        region: str,
        year: int | None,
    ) -> list[MonthlySalesRead]:
        return self.repo.list_monthly_sales_by_name(brand, category, region, year)
