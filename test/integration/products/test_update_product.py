# Third-Party library
import pytest

from src.controllers.product import ProductController


@pytest.mark.asyncio
async def test_update_product() -> None:
    old_product = {
        "name": "Product three",
        "description": "product description",
        "price": 20.11
    }

    product = await ProductController.create(old_product)
    product_id = product.get("product_id")

    new_product = {
        "name": "Product three",
        "description": "product three description",
        "price": 30.11
    }
    expected = {"success": True, "message": "Product updated"}

    result = await ProductController.update(product_id, new_product)

    assert result == expected


@pytest.mark.asyncio
async def test_find_product_product_not_found() -> None:
    product_id = 10

    expected = {
        "success": False,
        'message': 'Product not found'
    }
    new_product = {
        "name": "Product three",
        "description": "product three description",
        "price": 30.11
    }

    result = await ProductController.update(product_id, new_product)

    assert result == expected



