from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BusinessConsumptionOverTime(Base):
    __tablename__ = "business_consumption_over_time"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), index=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id"), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    month: Mapped[int] = mapped_column(Integer, index=True)
    agg_type_id: Mapped[int] = mapped_column(ForeignKey("agg_types.id"), index=True)
    value: Mapped[float] = mapped_column(Float)
