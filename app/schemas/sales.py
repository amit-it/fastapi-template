from pydantic import BaseModel


class MonthlySalesRead(BaseModel):
    year: int
    month: int
    units_sold: int
    revenue: float
    profit: float
