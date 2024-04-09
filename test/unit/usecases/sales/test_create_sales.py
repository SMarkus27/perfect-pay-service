from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.create_sales import CreateSales
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(SalesRepository, "create")
@patch.object(ProductRepository, "find_one_by_id")
async def test_create_sales(find_one_by_name_patch: Mock, create_patch: Mock):
    sales_repository = SalesRepository()
    product_repository = ProductRepository()

    sales = {
        "product": 2,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    sales_id = [{"id": 1}]

    find_one_by_name_patch.return_value = sales_id

    sales_with_id = sales.copy()
    sales_with_id["id"] = 1

    expected = {
        "success": True,
        "message": "sales created successfully",
        "data": sales_with_id,
    }

    create_patch.return_value = sales_with_id
    result = await CreateSales(sales_repository, product_repository).execute(sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ProductRepository, "find_one_by_id")
async def test_create_sales_product_not_found(find_one_by_id_patch: Mock):
    sales_repository = SalesRepository()
    product_repository = ProductRepository()

    sales = {
        "product": 2,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    product_id = []

    find_one_by_id_patch.return_value = product_id

    expected = {
        "success": False,
        "message": "Product not found",
    }

    result = await CreateSales(sales_repository, product_repository).execute(sales)

    assert result == expected
