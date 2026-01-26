from app.services.analytics_service import AnalyticsService
from datetime import date

def test_total_revenue_returns_number():
    result = AnalyticsService.total_revenue()
    assert isinstance(result, float)

def test_total_revenue_is_positive():
    result = AnalyticsService.total_revenue()
    assert result >= 0

def test_total_revenue_with_date_range():
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    result = AnalyticsService.total_revenue(start_date, end_date)
    assert isinstance(result, float)
    assert result >= 0

def test_total_revenue_with_no_data():
    start_date = date(1900, 1, 1)
    end_date = date(1900, 12, 31)
    result = AnalyticsService.total_revenue(start_date, end_date)
    assert result == 0.0

def test_get_daily_sales_structure():
    result = AnalyticsService.get_daily_sales()
    assert isinstance(result, list)
    if result:
        assert len(result[0]) == 3

def test_get_monthly_revenue_structure():
    result = AnalyticsService.get_monthly_revenue()
    assert isinstance(result, list)
    if result:
        assert len(result[0]) == 2