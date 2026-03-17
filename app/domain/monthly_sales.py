from dataclasses import dataclass


@dataclass(frozen=True)
class MonthlySales:
    year: int
    month: int
    units_sold: int
    revenue: float
    profit: float
