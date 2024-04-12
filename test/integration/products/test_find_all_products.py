# Standard library
from unittest.mock import patch, Mock

# Third-Party library
import pytest

from src.controllers.product import ProductController
from src.infra.repositories.product import ProductRepository


@pytest.mark.asyncio
async def test_find_all_products() -> None:
    result = await ProductController.find_all()
    assert len(result.get("data")) >= 1


@pytest.mark.asyncio
@patch.object(ProductRepository, "find")
async def test_find_all_products_products_not_found(find_patch: Mock) -> None:
    find_patch.return_value = []

    expected = {"success": False, "message": "Products not found"}
    result = await ProductController.find_all()

    assert result == expected
