import random
from datetime import date, timedelta

from app.core.database import SessionLocal
from app.models.brand import Brand
from app.models.category import Category
from app.models.region import Region
from app.models.sales_data import SalesFact
from app.models.segment import Segment
from app.models.sku import Sku
from app.models.subcategory import Subcategory


BRANDS = ["Acme", "Globex", "Umbrella", "Initech", "Soylent"]
CATEGORIES = ["Electronics", "Home", "Grocery", "Apparel", "Sports"]
SUBCATEGORIES = ["Phones", "Appliances", "Snacks", "Shoes", "Fitness"]
REGIONS = ["North", "South", "East", "West"]
SEGMENTS = ["Consumer", "Corporate", "Small Business"]
SKUS = [f"SKU-{i:04d}" for i in range(1, 51)]


def get_or_create_by_name(db, model, name: str):
    obj = db.query(model).filter(model.name == name).first()
    if obj:
        return obj
    obj = model(name=name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_or_create_sku(db, code: str):
    obj = db.query(Sku).filter(Sku.code == code).first()
    if obj:
        return obj
    obj = Sku(code=code)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def random_week_start(start: date, weeks: int) -> date:
    offset = random.randint(0, weeks - 1)
    return start + timedelta(days=7 * offset)


def seed_sales_data(count: int = 10000) -> None:
    db = SessionLocal()
    try:
        brands = [get_or_create_by_name(db, Brand, name) for name in BRANDS]
        categories = [get_or_create_by_name(db, Category, name) for name in CATEGORIES]
        subcategories = [get_or_create_by_name(db, Subcategory, name) for name in SUBCATEGORIES]
        regions = [get_or_create_by_name(db, Region, name) for name in REGIONS]
        segments = [get_or_create_by_name(db, Segment, name) for name in SEGMENTS]
        skus = [get_or_create_sku(db, code) for code in SKUS]

        start = date.today() - timedelta(weeks=104)
        rows = []
        for _ in range(count):
            units = random.randint(1, 200)
            price = round(random.uniform(5, 500), 2)
            discount = round(random.uniform(0, 0.3), 2)
            revenue = round(units * price * (1 - discount), 2)
            cost = round(revenue * random.uniform(0.4, 0.9), 2)
            profit = round(revenue - cost, 2)

            rows.append(
                SalesFact(
                    week_start=random_week_start(start, 104),
                    category_id=random.choice(categories).id,
                    subcategory_id=random.choice(subcategories).id,
                    region_id=random.choice(regions).id,
                    segment_id=random.choice(segments).id,
                    brand_id=random.choice(brands).id,
                    sku_id=random.choice(skus).id,
                    units_sold=units,
                    price=price,
                    discount=discount,
                    revenue=revenue,
                    cost=cost,
                    profit=profit,
                )
            )

        db.add_all(rows)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed_sales_data()
    print("Seeded sales_data.")
