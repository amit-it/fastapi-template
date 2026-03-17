from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BusinessTopScorecard(Base):
    __tablename__ = "business_top_scorecard"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), index=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id"), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    month: Mapped[int] = mapped_column(Integer, index=True)
    app_component_id: Mapped[int] = mapped_column(ForeignKey("app_components.id"), index=True)
    agg_type_id: Mapped[int] = mapped_column(ForeignKey("agg_types.id"), index=True)
    kpi_id: Mapped[int] = mapped_column(ForeignKey("kpis.id"), index=True)
    month_value: Mapped[float] = mapped_column(Float)
    month_growth: Mapped[float] = mapped_column(Float)
    quarterly_value: Mapped[float] = mapped_column(Float)
    quarterly_growth: Mapped[float] = mapped_column(Float)
    ytd_value: Mapped[float] = mapped_column(Float)
    ytd_growth: Mapped[float] = mapped_column(Float)
    category_change_monthly: Mapped[float] = mapped_column(Float)
    category_change_quarterly: Mapped[float] = mapped_column(Float)
    category_change_ytd: Mapped[float] = mapped_column(Float)
