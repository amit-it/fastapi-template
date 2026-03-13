import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base
from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact


@pytest.fixture()
def db_session():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(
        bind=engine,
        tables=[
            Brand.__table__,
            Category.__table__,
            Region.__table__,
            SalesFact.__table__,
        ],
    )
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
