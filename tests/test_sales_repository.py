from datetime import date

from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact
from app.repositories.sales import SqlAlchemySalesRepository
from app.services.sales import SalesService


def seed_sales(db):
    brand = Brand(name="Acme")
    category = Category(name="Electronics")
    region = Region(name="North")
    db.add_all([brand, category, region])
    db.commit()
    db.refresh(brand)
    db.refresh(category)
    db.refresh(region)

    db.add_all(
        [
            SalesFact(
                week_start=date(2025, 1, 6),
                category_id=category.id,
                subcategory_id=1,
                region_id=region.id,
                segment_id=1,
                brand_id=brand.id,
                sku_id=1,
                units_sold=10,
                price=100.0,
                discount=0.1,
                revenue=900.0,
                cost=500.0,
                profit=400.0,
            ),
            SalesFact(
                week_start=date(2025, 1, 13),
                category_id=category.id,
                subcategory_id=1,
                region_id=region.id,
                segment_id=1,
                brand_id=brand.id,
                sku_id=1,
                units_sold=5,
                price=100.0,
                discount=0.0,
                revenue=500.0,
                cost=200.0,
                profit=300.0,
            ),
            SalesFact(
                week_start=date(2025, 2, 3),
                category_id=category.id,
                subcategory_id=1,
                region_id=region.id,
                segment_id=1,
                brand_id=brand.id,
                sku_id=1,
                units_sold=3,
                price=50.0,
                discount=0.0,
                revenue=150.0,
                cost=80.0,
                profit=70.0,
            ),
        ]
    )
    db.commit()


def test_sales_repository_monthly(db_session):
    seed_sales(db_session)
    repo = SqlAlchemySalesRepository(db_session)

    rows = repo.list_monthly_sales_by_name("Acme", "Electronics", "North", 2025)

    assert len(rows) == 2
    jan = rows[0]
    feb = rows[1]
    assert (jan.year, jan.month) == (2025, 1)
    assert jan.units_sold == 15
    assert jan.revenue == 1400.0
    assert jan.profit == 700.0
    assert (feb.year, feb.month) == (2025, 2)
    assert feb.units_sold == 3


def test_sales_service_delegates(db_session):
    repo = SqlAlchemySalesRepository(db_session)
    service = SalesService(repo)
    result = service.list_monthly_sales_by_name("x", "y", "z", None)
    assert result == []


def test_sales_repository_filters_by_year(db_session):
    seed_sales(db_session)
    repo = SqlAlchemySalesRepository(db_session)

    rows = repo.list_monthly_sales_by_name("Acme", "Electronics", "North", 2024)

    assert rows == []
