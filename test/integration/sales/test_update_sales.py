# Third-Party library
import pytest

from src.controllers.sales import SalesController


@pytest.mark.asyncio
async def test_update_sales() -> None:
    old_product = {
        "product": 1,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": False
    }

    product = await SalesController.create(old_product)
    data = product.get("data")[0]
    product_id = data.get("id")

    new_product = {
        "product": 1,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    result = await SalesController.update(product_id, new_product)

    assert result.get("data")[0] != old_product


@pytest.mark.asyncio
async def test_find_sales_client_not_found() -> None:
    sales_id = 1

    expected = {"success": False, "message": "Client not found"}
    new_sales = {
        "product": 1,
        "client": 10,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    result = await SalesController.update(sales_id, new_sales)

    assert result == expected


@pytest.mark.asyncio
async def test_find_sales_product_not_found() -> None:
    sales_id = 100

    expected = {"success": False, "message": "Product not found"}
    new_sales = {
        "product": 100,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    result = await SalesController.update(sales_id, new_sales)
    print(result)
    assert result == expected


@pytest.mark.asyncio
async def test_find_sales_sales_not_found() -> None:
    sales_id = 100

    expected = {"success": False, "message": "Sales not found"}
    new_sales = {
        "product": 1,
        "client": 1,
        "sales_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    result = await SalesController.update(sales_id, new_sales)

    assert result == expected
