from sqlalchemy import extract, func, select
from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact
from app.schemas.sales import MonthlySalesRead


class SqlAlchemySalesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_monthly_sales_by_name(
        self,
        brand: str,
        category: str,
        region: str,
        year: int | None,
    ) -> list[MonthlySalesRead]:
        year_col = extract("year", SalesFact.week_start).label("year")
        month_col = extract("month", SalesFact.week_start).label("month")
        stmt = (
            select(
                year_col,
                month_col,
                func.sum(SalesFact.units_sold).label("units_sold"),
                func.sum(SalesFact.revenue).label("revenue"),
                func.sum(SalesFact.profit).label("profit"),
            )
            .join(Brand, SalesFact.brand_id == Brand.id)
            .join(Category, SalesFact.category_id == Category.id)
            .join(Region, SalesFact.region_id == Region.id)
            .where(
                Brand.name == brand,
                Category.name == category,
                Region.name == region,
            )
            .group_by(year_col, month_col)
            .order_by(year_col, month_col)
        )
        if year is not None:
            stmt = stmt.where(extract("year", SalesFact.week_start) == year)

        rows = self.db.execute(stmt).all()
        return [
            MonthlySalesRead(
                year=int(row.year or 0),
                month=int(row.month or 0),
                units_sold=int(row.units_sold or 0),
                revenue=float(row.revenue or 0),
                profit=float(row.profit or 0),
            )
            for row in rows
        ]
