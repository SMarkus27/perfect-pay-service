# Third-Party library
import pytest

from src.controllers.product import ProductController


@pytest.mark.asyncio
async def test_create_product() -> None:
    new_product = {
        "name": "Product one",
        "description": "product description",
        "price": 20.11,
    }
    result = await ProductController.create(new_product)
    data = result.get("data")[0]
    assert int(data.get("id")) >= 0


@pytest.mark.asyncio
async def test_create_product_product_already_created() -> None:
    new_product = {
        "name": "Product one",
        "description": "product description",
        "price": 20.11,
    }

    expected = {"success": False, "message": "Product already exist"}
    result = await ProductController.create(new_product)

    assert result == expected
