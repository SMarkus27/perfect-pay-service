import pytest

from src.domain.entities.sales import Sales


def test_correct_sales():
    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }
    Sales(**sales)


def test_invalid_product():
    sales = {
        "product": 0,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }
    with pytest.raises(Exception) as e:
        Sales(**sales)


def test_invalid_client():
    sales = {
        "product": 2,
        "client": 0,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": "True"
    }
    with pytest.raises(Exception) as e:
        Sales(**sales)


def test_invalid_quantity():
    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 0,
        "discount": 0.5,
        "status": True
    }
    with pytest.raises(Exception) as e:
        Sales(**sales)


def test_invalid_discount():
    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": -0.5,
        "status": True
    }
    with pytest.raises(Exception) as e:
        Sales(**sales)


def test_invalid_status():
    sales = {
        "product": 2,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": "True"
    }
    with pytest.raises(Exception) as e:
        Sales(**sales)
