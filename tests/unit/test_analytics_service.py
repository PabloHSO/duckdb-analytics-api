from app.services.analytics_service import AnalyticsService
from datetime import date

def test_total_revenue_returns_number(monkeypatch, duckdb_conn):
    monkeypatch.setattr(
        "app.services.analytics_service.get_connection",
        lambda: duckdb_conn
    )

    result = AnalyticsService.total_revenue()
    assert result == 300.0


def test_total_revenue_is_positive(monkeypatch, duckdb_conn):
    monkeypatch.setattr(
        "app.services.analytics_service.get_connection",
        lambda: duckdb_conn
    )

    result = AnalyticsService.total_revenue()
    assert result >= 0


def test_total_revenue_with_date_range(monkeypatch, duckdb_conn):
    monkeypatch.setattr(
        "app.services.analytics_service.get_connection",
        lambda: duckdb_conn
    )

    result = AnalyticsService.total_revenue(
        date(2023, 1, 1),
        date(2023, 12, 31)
    )
    assert isinstance(result, float)


def test_total_revenue_with_no_data(monkeypatch, duckdb_conn):
    monkeypatch.setattr(
        "app.services.analytics_service.get_connection",
        lambda: duckdb_conn
    )

    result = AnalyticsService.total_revenue(
        date(1900, 1, 1),
        date(1900, 12, 31)
    )
    assert result == 0.0
