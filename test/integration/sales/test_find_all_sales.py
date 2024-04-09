# Standard library
from unittest.mock import patch, Mock

# Third-Party library
import pytest

from src.controllers.sales import SalesController
from src.infra.repositories.sales import SalesRepository


@pytest.mark.asyncio
async def test_find_all_sales() -> None:
    result = await SalesController.find_all()
    assert len(result.get("data")) >= 1


@pytest.mark.asyncio
@patch.object(SalesRepository, "find")
async def test_find_all_sales_sales_not_found(find_patch: Mock) -> None:
    find_patch.return_value = []

    expected = {"success": False, "message": "Sales not found"}
    result = await SalesController.find_all()

    assert result == expected
