from unittest.mock import patch, Mock

import pytest

from src.application.usecases.products.create_product import CreateProduct
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
@patch.object(ProductRepository, "create")
@patch.object(ProductRepository, "find_one_by_name")
async def test_create_product(find_one_by_name_patch: Mock, create_patch: Mock):
    product_repository = ProductRepository()
    product = {
        "name": "Test Product",
        "description": "Product Description",
        "price": 55.11,
    }

    product_id = []

    find_one_by_name_patch.return_value = product_id

    product_with_id = product.copy()
    product_with_id["id"] = 1

    expected = {
        "success": True,
        "message": "product created successfully",
        "data": product_with_id,
    }

    create_patch.return_value = product_with_id
    result = await CreateProduct(product_repository).execute(product)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_name")
async def test_create_product_product_already_exists(find_one_by_name_patch: Mock):
    product_repository = ProductRepository()
    product = {
        "name": "Test Product",
        "description": "Product Description",
        "price": 55.11,
    }

    product_id = [{"id": 1}]

    find_one_by_name_patch.return_value = product_id

    expected = {
        "success": False,
        "message": "Product already exist",
    }

    result = await CreateProduct(product_repository).execute(product)

    assert result == expected
