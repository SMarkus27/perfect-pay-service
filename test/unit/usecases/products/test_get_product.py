from unittest.mock import patch, Mock

import pytest

from src.application.usecases.products.get_product import GetProduct
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
async def test_get_product(find_one_by_id_patch: Mock):
    product_repository = ProductRepository()
    product_id = 1
    products = [
        {"name": "product one",
         "description": "product description",
         "price": 10.22,
         "id": 1
         },
    ]
    find_one_by_id_patch.return_value = products

    expected = {
                "success": True,
                "data": products
            }

    result = await GetProduct(product_repository).execute(product_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
async def test_get_product_product_not_found(find_one_by_id_patch: Mock):
    product_repository = ProductRepository()
    product_id = 100

    find_one_by_id_patch.return_value = []

    expected = {
                "success": False,
                "message": "Product not found"
            }

    result = await GetProduct(product_repository).execute(product_id)

    assert result == expected
