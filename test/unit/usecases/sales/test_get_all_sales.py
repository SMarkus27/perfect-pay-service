from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.get_all_sales import GetAllSales
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(SalesRepository, "find")
async def test_get_all_sales(find_patch: Mock):
    sales_repository = SalesRepository()
    sales = [
        {
            "product": 2,
            "sales_date": "2024-02-02",
            "quantity": 5,
            "discount": 0.5,
            "status": True
        },
        {
            "product": 2,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        },
    ]
    find_patch.return_value = sales

    expected = {"success": True, "data": sales}

    result = await GetAllSales(sales_repository).execute()

    assert result == expected


@pytest.mark.asyncio
@patch.object(SalesRepository, "find")
async def test_get_all_sales_sales_not_found(find_patch: Mock):
    sales_repository = SalesRepository()

    find_patch.return_value = []

    expected = {"success": False, "message": "Sales not found"}

    result = await GetAllSales(sales_repository).execute()

    assert result == expected
