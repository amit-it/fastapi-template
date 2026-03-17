from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict


class SalesDataCreate(BaseModel):
    week_start: date
    category_id: int
    subcategory_id: int
    region_id: int
    segment_id: int
    brand_id: int
    sku_id: int
    units_sold: int
    price: float
    discount: float
    revenue: float
    cost: float
    profit: float


class SalesDataRead(SalesDataCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
