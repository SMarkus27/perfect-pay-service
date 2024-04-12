from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.delete_sales import DeleteSales
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(SalesRepository, "delete")
@patch.object(SalesRepository, "find_one_by_id")
async def test_delete_product(find_one_by_id_patch: Mock, delete_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 2
    product_id = 1

    find_one_by_id_patch.return_value = [{"id": product_id}]

    expected = {
        "success": True,
        "message": "Sales deleted successfully",
    }

    result = await DeleteSales(sales_repository).execute(sales_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(SalesRepository, "find_one_by_id")
async def test_delete_sales_sales_not_found(find_one_by_id_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 100

    find_one_by_id_patch.return_value = []

    expected = {
        "success": False,
        "message": "Sales not found",
    }

    result = await DeleteSales(sales_repository).execute(sales_id)

    assert result == expected
