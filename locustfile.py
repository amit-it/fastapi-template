from locust import HttpUser, between, task


class ApiUser(HttpUser):
    wait_time = between(0.5, 2.0)

    @task(3)
    def health(self):
        self.client.get("/health/")

    @task(2)
    def sales_monthly(self):
        self.client.get(
            "/sales/monthly",
            params={"brand": "Acme", "category": "Electronics", "region": "North"},
        )

    @task(1)
    def business_kpi(self):
        self.client.get(
            "/business-kpi",
            params={"year": 2025, "month": 1, "brand": "Acme", "category": "Phones"},
        )
