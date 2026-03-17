from dataclasses import dataclass


@dataclass(frozen=True)
class BusinessKpi:
    brand: str
    sub_category: str
    year: int
    month: int
    app_component: str
    type_of_agg: str
    kpi: str
    month_value: float
    month_growth: float
    quarterly_value: float
    quarterly_growth: float
    ytd_value: float
    ytd_growth: float
    category_change_monthly: float
    category_change_quarterly: float
    category_change_ytd: float
