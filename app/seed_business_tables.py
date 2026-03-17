from app.core.database import SessionLocal
from app.models.agg_type import AggType
from app.models.app_component import AppComponent
from app.models.brand import Brand
from app.models.business_consumption_over_time import BusinessConsumptionOverTime
from app.models.business_health_scorecard import BusinessHealthScorecard
from app.models.business_sku_level import BusinessSkuLevel
from app.models.business_top_scorecard import BusinessTopScorecard
from app.models.kpi import Kpi
from app.models.ppg import Ppg
from app.models.sku import Sku
from app.models.subcategory import Subcategory


SAMPLE_BRANDS = ["Acme", "Globex"]
SAMPLE_SUBCATEGORIES = ["Phones", "Appliances"]
SAMPLE_APP_COMPONENTS = ["Dashboard", "Insights"]
SAMPLE_AGG_TYPES = ["SUM", "AVG"]
SAMPLE_KPIS = ["Revenue", "Profit"]
SAMPLE_PPGS = [("PPG-001", "Starter Pack"), ("PPG-002", "Pro Pack")]
SAMPLE_SKUS = ["SKU-1001", "SKU-1002"]


def get_or_create_by_name(db, model, name: str):
    obj = db.query(model).filter(model.name == name).first()
    if obj:
        return obj
    obj = model(name=name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_or_create_ppg(db, code: str, description: str):
    obj = db.query(Ppg).filter(Ppg.code == code).first()
    if obj:
        return obj
    obj = Ppg(code=code, description=description)
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


def seed_business_tables(count: int = 100000) -> None:
    db = SessionLocal()
    try:
        brands = [get_or_create_by_name(db, Brand, name) for name in SAMPLE_BRANDS]
        subcategories = [
            get_or_create_by_name(db, Subcategory, name) for name in SAMPLE_SUBCATEGORIES
        ]
        app_components = [
            get_or_create_by_name(db, AppComponent, name) for name in SAMPLE_APP_COMPONENTS
        ]
        agg_types = [get_or_create_by_name(db, AggType, name) for name in SAMPLE_AGG_TYPES]
        kpis = [get_or_create_by_name(db, Kpi, name) for name in SAMPLE_KPIS]
        ppgs = [get_or_create_ppg(db, code, desc) for code, desc in SAMPLE_PPGS]
        skus = [get_or_create_sku(db, code) for code in SAMPLE_SKUS]

        bco_rows = []
        bhs_rows = []
        bts_rows = []
        bsl_rows = []

        for i in range(count):
            brand = brands[i % len(brands)]
            subcategory = subcategories[i % len(subcategories)]
            app_component = app_components[i % len(app_components)]
            agg_type = agg_types[i % len(agg_types)]
            kpi = kpis[i % len(kpis)]
            ppg = ppgs[i % len(ppgs)]
            sku = skus[i % len(skus)]
            month = (i % 12) + 1

            bco_rows.append(
                BusinessConsumptionOverTime(
                    brand_id=brand.id,
                    subcategory_id=subcategory.id,
                    year=2025,
                    month=month,
                    agg_type_id=agg_type.id,
                    value=1000.0,
                )
            )
            bhs_rows.append(
                BusinessHealthScorecard(
                    brand_id=brand.id,
                    subcategory_id=subcategory.id,
                    year=2025,
                    month=month,
                    agg_type_id=agg_type.id,
                    kpi_id=kpi.id,
                    ytd_value=5000.0,
                    py_growth=0.1,
                    category_avg_ytd=4800.0,
                )
            )
            bts_rows.append(
                BusinessTopScorecard(
                    brand_id=brand.id,
                    subcategory_id=subcategory.id,
                    year=2025,
                    month=month,
                    app_component_id=app_component.id,
                    agg_type_id=agg_type.id,
                    kpi_id=kpi.id,
                    month_value=1000.0,
                    month_growth=0.05,
                    quarterly_value=3000.0,
                    quarterly_growth=0.08,
                    ytd_value=8000.0,
                    ytd_growth=0.12,
                    category_change_monthly=0.02,
                    category_change_quarterly=0.03,
                    category_change_ytd=0.04,
                )
            )
            bsl_rows.append(
                BusinessSkuLevel(
                    brand_id=brand.id,
                    subcategory_id=subcategory.id,
                    year=2025,
                    month=month,
                    ppg_id=ppg.id,
                    sku_id=sku.id,
                    autoship_contribution=200.0,
                    non_autoship_contribution=150.0,
                )
            )

        db.add_all(bco_rows)
        db.add_all(bhs_rows)
        db.add_all(bts_rows)
        db.add_all(bsl_rows)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed_business_tables()
    print("Seeded business tables.")
