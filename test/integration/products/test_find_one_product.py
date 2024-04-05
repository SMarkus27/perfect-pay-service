# Third-Party library
import pytest

from src.controllers.product import ProductController


@pytest.mark.asyncio
async def test_find_one_product() -> None:
    product_id = 1
    result = await ProductController.find_one(product_id)

    assert len(result.get("data")) == 1


@pytest.mark.asyncio
async def test_find_product_product_not_found() -> None:
    product_id = 10

    expected = {
        "success": False,
        'message': 'Product not found'
    }
    result = await ProductController.find_one(product_id)

    assert result == expected



