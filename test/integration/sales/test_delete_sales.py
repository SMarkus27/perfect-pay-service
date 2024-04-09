import pytest

from src.controllers.sales import SalesController


@pytest.mark.asyncio
async def test_delete_sales() -> None:
    new_sales = {
        "product": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    sales = await SalesController.create(new_sales)
    data = sales.get("data")[0]
    sales_id = data.get("id")
    expected = {"success": True, "message": "Sales deleted successfully"}

    result = await SalesController.delete(sales_id)

    assert result == expected


@pytest.mark.asyncio
async def test_delete_sales_sales_not_found() -> None:
    sales_id = 100

    expected = {"success": False, "message": "Sales not found"}
    result = await SalesController.delete(sales_id)
    assert result == expected
