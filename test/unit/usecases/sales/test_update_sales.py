from unittest.mock import patch, Mock

import pytest

from src.application.usecases.sales.update_sales import UpdateSales
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
@patch.object(SalesRepository, "update")
@patch.object(SalesRepository, "find_one_by_id")
async def test_update_sales(find_one_by_id_patch: Mock, update_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 1

    new_sales = {
        "product": 2,
        "sales_date": "2024-02-03",
        "quantity": 50,
        "discount": 0.65,
        "status": False
    }
    find_one_by_id_patch.return_value = new_sales

    expected = {"success": True, "message": "Sales updated", "data": new_sales}
    update_patch.return_value = new_sales
    result = await UpdateSales(sales_repository).execute(sales_id, new_sales)

    assert result == expected


@pytest.mark.asyncio
@patch.object(SalesRepository, "find_one_by_id")
async def test_update_sales_sales_not_found(find_one_by_id_patch: Mock):
    sales_repository = SalesRepository()
    sales_id = 100

    new_sales = (
        {
            "product": 2,
            "sales_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        },
    )

    find_one_by_id_patch.return_value = []

    expected = {"success": False, "message": "Sales not found"}

    result = await UpdateSales(sales_repository).execute(sales_id, new_sales)

    assert result == expected
