import pytest

from src.domain.entities.product import Product


def test_correct_name():
    product = {
        "name": "Product One",
        "description": "Description Product one",
        "price": 20.11
    }
    Product(**product)


def test_invalid_name():
    product = {
        "name": "One",
        "description": "Description Product one",
        "price": 20.11
    }
    with pytest.raises(Exception) as e:
        Product(**product)


def test_correct_description():
    product = {
        "name": "Product One",
        "description": "Description Product one",
        "price": 20.11
    }
    Product(**product)


def test_invalid_description():
    product = {
        "name": "Product One",
        "description": "one",
        "price": 20.11
    }
    with pytest.raises(Exception) as e:
        Product(**product)


def test_correct_price():
    product = {
        "name": "Product One",
        "description": "Product One",
        "price": 20.11
    }
    Product(**product)


def test_invalid_price():
    product = {
        "name": "Product One",
        "description": "Product One",
        "price": 0
    }
    with pytest.raises(Exception) as e:
        Product(**product)