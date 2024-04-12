from unittest.mock import patch, Mock

import pytest

from src.application.usecases.products.delete_product import DeleteProduct
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "delete")
@patch.object(ProductRepository, "find_one_by_id")
async def test_delete_product(find_one_by_id_patch: Mock, delete_patch: Mock):
    product_repository = ProductRepository()
    product_id = 1

    find_one_by_id_patch.return_value = [
        {
            "name": "Product One",
            "description": "Product Description",
            "price": 55.12,
            "id": product_id,
        }
    ]

    expected = {
        "success": True,
        "message": "Product deleted successfully",
    }

    result = await DeleteProduct(product_repository).execute(product_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
async def test_delete_product_product_not_found(find_one_by_id_patch: Mock):
    product_repository = ProductRepository()
    product_id = 100

    find_one_by_id_patch.return_value = []

    expected = {
        "success": False,
        "message": "Product not found",
    }

    result = await DeleteProduct(product_repository).execute(product_id)

    assert result == expected
