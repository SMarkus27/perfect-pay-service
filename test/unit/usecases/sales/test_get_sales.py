from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.get_sales import GetSales
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(SalesRepository, "find_one_by_id")
async def test_get_sales(find_one_by_id_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 1
    sales = [
        {
            "product": 2,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        },
    ]
    find_one_by_id_patch.return_value = sales

    expected = {"success": True, "data": sales}

    result = await GetSales(sales_repository).execute(sales_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(SalesRepository, "find_one_by_id")
async def test_get_sales_sales_not_found(find_one_by_id_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 100

    find_one_by_id_patch.return_value = []

    expected = {"success": False, "message": "Sales not found"}

    result = await GetSales(sales_repository).execute(sales_id)

    assert result == expected
