from app.core.config import Settings


def test_database_url_building():
    settings = Settings(
        mysql_host="db",
        mysql_port=3307,
        mysql_user="user",
        mysql_password="pass",
        mysql_db="sales",
    )
    assert settings.database_url == "mysql+pymysql://user:pass@db:3307/sales"
