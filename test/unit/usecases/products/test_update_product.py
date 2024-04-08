from unittest.mock import patch, Mock

import pytest

from src.application.usecases.products.update_product import UpdateProduct
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "update")
@patch.object(ProductRepository, "find_one_by_id")
async def test_update_product(find_one_by_id_patch: Mock, update_patch: Mock):
    product_repository = ProductRepository()
    product_id = 1

    new_product = {
        "name": "new product one",
        "description": "product description",
        "price": 11.22
    }
    find_one_by_id_patch.return_value = new_product

    expected = {
                "success": True,
                "message": "Product updated",
                "data": new_product
            }
    update_patch.return_value = new_product
    result = await UpdateProduct(product_repository).execute(product_id, new_product)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
async def test_update_product_product_not_found(find_one_by_id_patch: Mock):
    product_repository = ProductRepository()
    product_id = 100

    new_product = {
        "name": "new product one",
        "description": "product description",
        "price": 11.22,
        },

    find_one_by_id_patch.return_value = []

    expected = {
                "success": False,
                "message": "Product not found"
            }

    result = await UpdateProduct(product_repository).execute(product_id, new_product)

    assert result == expected
