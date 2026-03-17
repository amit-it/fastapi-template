from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.business_kpi import BusinessKpi
from app.models.agg_type import AggType
from app.models.app_component import AppComponent
from app.models.brand import Brand
from app.models.business_top_scorecard import BusinessTopScorecard
from app.models.kpi import Kpi
from app.models.subcategory import Subcategory
from app.repositories.business_kpi_interfaces import BusinessKpiRepository


class SqlAlchemyBusinessKpiRepository(BusinessKpiRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_business_kpi(
        self,
        year: int,
        month: int,
        brand: str,
        category: str,
    ) -> list[BusinessKpi]:
        stmt = (
            select(
                Brand.name.label("brand"),
                Subcategory.name.label("sub_category"),
                BusinessTopScorecard.year,
                BusinessTopScorecard.month,
                AppComponent.name.label("app_component"),
                AggType.name.label("type_of_agg"),
                Kpi.name.label("kpi"),
                BusinessTopScorecard.month_value,
                BusinessTopScorecard.month_growth,
                BusinessTopScorecard.quarterly_value,
                BusinessTopScorecard.quarterly_growth,
                BusinessTopScorecard.ytd_value,
                BusinessTopScorecard.ytd_growth,
                BusinessTopScorecard.category_change_monthly,
                BusinessTopScorecard.category_change_quarterly,
                BusinessTopScorecard.category_change_ytd,
            )
            .join(Brand, BusinessTopScorecard.brand_id == Brand.id)
            .join(Subcategory, BusinessTopScorecard.subcategory_id == Subcategory.id)
            .join(AppComponent, BusinessTopScorecard.app_component_id == AppComponent.id)
            .join(AggType, BusinessTopScorecard.agg_type_id == AggType.id)
            .join(Kpi, BusinessTopScorecard.kpi_id == Kpi.id)
            .where(
                BusinessTopScorecard.year == year,
                BusinessTopScorecard.month == month,
                Brand.name == brand,
                Subcategory.name == category,
            )
        )

        rows = self.db.execute(stmt).all()
        return [
            BusinessKpi(
                brand=row.brand,
                sub_category=row.sub_category,
                year=row.year,
                month=row.month,
                app_component=row.app_component,
                type_of_agg=row.type_of_agg,
                kpi=row.kpi,
                month_value=float(row.month_value),
                month_growth=float(row.month_growth),
                quarterly_value=float(row.quarterly_value),
                quarterly_growth=float(row.quarterly_growth),
                ytd_value=float(row.ytd_value),
                ytd_growth=float(row.ytd_growth),
                category_change_monthly=float(row.category_change_monthly),
                category_change_quarterly=float(row.category_change_quarterly),
                category_change_ytd=float(row.category_change_ytd),
            )
            for row in rows
        ]
