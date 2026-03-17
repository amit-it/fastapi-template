from contextlib import asynccontextmanager

from app.core import database
from app.schemas.sales_data import SalesDataCreate, SalesDataRead


@asynccontextmanager
async def _no_db_lifespan(_: object):
    yield


def test_main_imports_app():
    from app import main

    main.app.router.lifespan_context = _no_db_lifespan
    assert main.app is not None


def test_get_db_closes_session(monkeypatch):
    closed = {"value": False}

    class DummySession:
        def close(self):
            closed["value"] = True

    monkeypatch.setattr(database, "SessionLocal", lambda: DummySession())

    gen = database.get_db()
    session = next(gen)
    assert isinstance(session, DummySession)
    try:
        next(gen)
    except StopIteration:
        pass

    assert closed["value"] is True


def test_deps_provide_sales_services(db_session):
    from app.api import deps

    repo = deps.get_sales_repository(db_session)
    service = deps.get_sales_service(repo)

    assert repo is not None
    assert service is not None


def test_sales_data_schema_roundtrip():
    payload = SalesDataCreate(
        week_start="2025-01-01",
        category_id=1,
        subcategory_id=2,
        region_id=3,
        segment_id=4,
        brand_id=5,
        sku_id=6,
        units_sold=10,
        price=100.0,
        discount=0.1,
        revenue=900.0,
        cost=500.0,
        profit=400.0,
    )
    read = SalesDataRead(id=1, **payload.model_dump())
    assert read.id == 1
