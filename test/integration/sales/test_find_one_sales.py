# Third-Party library
import pytest

from src.controllers.sales import SalesController


@pytest.mark.asyncio
async def test_find_one_sales() -> None:
    sales_id = 1
    result = await SalesController.find_one(sales_id)
    assert len(result.get("data")) == 1


@pytest.mark.asyncio
async def test_find_sales_sales_not_found() -> None:
    sales_id = 10

    expected = {"success": False, "message": "Sales not found"}
    result = await SalesController.find_one(sales_id)

    assert result == expected
