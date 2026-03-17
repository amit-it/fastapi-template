from abc import ABC, abstractmethod

from app.domain.monthly_sales import MonthlySales


class SalesService(ABC):
    @abstractmethod
    def list_monthly_sales_by_name(
        self,
        brand: str,
        category: str,
        region: str,
        year: int | None,
    ) -> list[MonthlySales]:
        raise NotImplementedError
