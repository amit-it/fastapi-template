from app.domain.business_kpi import BusinessKpi
from app.domain.monthly_sales import MonthlySales
from app.schemas.business_kpi import BusinessKpiRead
from app.schemas.sales import MonthlySalesRead


def to_monthly_sales_read(items: list[MonthlySales]) -> list[MonthlySalesRead]:
    return [
        MonthlySalesRead(
            year=item.year,
            month=item.month,
            units_sold=item.units_sold,
            revenue=item.revenue,
            profit=item.profit,
        )
        for item in items
    ]


def to_business_kpi_read(items: list[BusinessKpi]) -> list[BusinessKpiRead]:
    return [
        BusinessKpiRead(
            brand=item.brand,
            sub_category=item.sub_category,
            year=item.year,
            month=item.month,
            app_component=item.app_component,
            type_of_agg=item.type_of_agg,
            kpi=item.kpi,
            month_value=item.month_value,
            month_growth=item.month_growth,
            quarterly_value=item.quarterly_value,
            quarterly_growth=item.quarterly_growth,
            ytd_value=item.ytd_value,
            ytd_growth=item.ytd_growth,
            category_change_monthly=item.category_change_monthly,
            category_change_quarterly=item.category_change_quarterly,
            category_change_ytd=item.category_change_ytd,
        )
        for item in items
    ]
