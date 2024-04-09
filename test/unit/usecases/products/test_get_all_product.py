from unittest.mock import patch, Mock

import pytest

from src.application.usecases.products.get_all_products import GetAllProducts
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "find")
async def test_get_all_products(find_patch: Mock):
    product_repository = ProductRepository()
    products = [
        {
            "name": "product one",
            "description": "product description",
            "price": 10.22,
            "id": 1,
        },
        {
            "name": "product two",
            "description": "product description",
            "price": 51.00,
            "id": 2,
        },
    ]
    find_patch.return_value = products

    expected = {"success": True, "data": products}

    result = await GetAllProducts(product_repository).execute()

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find")
async def test_get_all_products_products_not_found(find_patch: Mock):
    product_repository = ProductRepository()

    find_patch.return_value = []

    expected = {"success": False, "message": "Products not found"}

    result = await GetAllProducts(product_repository).execute()

    assert result == expected
