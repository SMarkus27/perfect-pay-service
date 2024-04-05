import pytest

from src.controllers.product import ProductController


@pytest.mark.asyncio
async def test_delete_product() -> None:
    new_product = {
        "name": "Product four",
        "description": "product description",
        "price": 20.11
    }

    product = await ProductController.create(new_product)
    product_id = product.get("product_id")
    expected = {"success": True, "message": "Product deleted successfully"}

    result = await ProductController.delete(product_id)

    assert result == expected


@pytest.mark.asyncio
async def test_delete_product_product_not_found() -> None:
    product_id = 100

    expected = {
        "success": False,
        'message': 'Product not found'
    }
    result = await ProductController.delete(product_id)
    print(result)
    assert result == expected



