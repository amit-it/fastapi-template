from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BusinessHealthScorecard(Base):
    __tablename__ = "business_health_scorecard"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), index=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id"), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    month: Mapped[int] = mapped_column(Integer, index=True)
    agg_type_id: Mapped[int] = mapped_column(ForeignKey("agg_types.id"), index=True)
    kpi_id: Mapped[int] = mapped_column(ForeignKey("kpis.id"), index=True)
    ytd_value: Mapped[float] = mapped_column(Float)
    py_growth: Mapped[float] = mapped_column(Float)
    category_avg_ytd: Mapped[float] = mapped_column(Float)
