from fastapi.testclient import TestClient

from app.factory import create_app
from app.schemas.sales import MonthlySalesRead


def test_health_endpoint():
    app = create_app()

    app.router.on_startup.clear()

    client = TestClient(app)
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sales_monthly_endpoint_override():
    app = create_app()

    app.router.on_startup.clear()

    def _override_service():
        class Stub:
            def list_monthly_sales_by_name(self, brand, category, region, year):
                return [
                    MonthlySalesRead(
                        year=2025,
                        month=1,
                        units_sold=10,
                        revenue=1000.0,
                        profit=250.0,
                    )
                ]

        return Stub()

    from app.api.deps import get_sales_service

    app.dependency_overrides[get_sales_service] = _override_service
    client = TestClient(app)

    response = client.get(
        "/sales/monthly",
        params={"brand": "Acme", "category": "Electronics", "region": "North"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload[0]["year"] == 2025
    assert payload[0]["month"] == 1
