import random
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base
from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact
from app.models.segment import Segment
from app.models.sku import Sku
from app.models.subcategory import Subcategory


def test_seed_sales_data(monkeypatch):
    engine = create_engine("sqlite+pysqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(
        bind=engine,
        tables=[
            Brand.__table__,
            Category.__table__,
            Subcategory.__table__,
            Region.__table__,
            Segment.__table__,
            Sku.__table__,
            SalesFact.__table__,
        ],
    )

    from app import seed_sales_data as seed_module

    monkeypatch.setattr(seed_module, "SessionLocal", SessionLocal)
    monkeypatch.setattr(seed_module.random, "randint", lambda a, b: a)
    monkeypatch.setattr(seed_module.random, "uniform", lambda a, b: a)

    seed_module.seed_sales_data(count=5)

    session = SessionLocal()
    try:
        count = session.query(SalesFact).count()
        assert count == 5
    finally:
        session.close()
