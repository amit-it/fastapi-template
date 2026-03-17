from abc import ABC, abstractmethod

from app.domain.business_kpi import BusinessKpi


class BusinessKpiRepository(ABC):
    @abstractmethod
    def list_business_kpi(
        self,
        year: int,
        month: int,
        brand: str,
        category: str,
    ) -> list[BusinessKpi]:
        raise NotImplementedError
