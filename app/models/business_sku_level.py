from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BusinessSkuLevel(Base):
    __tablename__ = "business_sku_level"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"), index=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id"), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    month: Mapped[int] = mapped_column(Integer, index=True)
    ppg_id: Mapped[int] = mapped_column(ForeignKey("ppgs.id"), index=True)
    sku_id: Mapped[int] = mapped_column(ForeignKey("skus.id"), index=True)
    autoship_contribution: Mapped[float] = mapped_column(Float)
    non_autoship_contribution: Mapped[float] = mapped_column(Float)
