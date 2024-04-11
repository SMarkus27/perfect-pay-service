# Third-Party library
import pytest

from src.controllers.sales import SalesController


@pytest.mark.asyncio
async def test_create_sales() -> None:
    new_sales = {
        "product": 1,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }
    result = await SalesController.create(new_sales)
    data = result.get("data")[0]
    assert int(data.get("id")) >= 0


@pytest.mark.asyncio
async def test_create_sales_product_not_found() -> None:
    new_sales = {
        "product": 5,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    expected = {"success": False, "message": "Product not found"}
    result = await SalesController.create(new_sales)

    assert result == expected
