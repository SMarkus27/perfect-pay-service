# Standard library
from unittest.mock import patch, Mock

# Third-Party library
import pytest

from src.controllers.client import ClientController
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
async def test_find_all_client() -> None:
    result = await ClientController.find_all()
    assert len(result.get("data")) >= 1


@pytest.mark.asyncio
@patch.object(ClientRepository, "find")
async def test_find_all_client_client_not_found(find_patch: Mock) -> None:
    find_patch.return_value = []

    expected = {"success": False, "message": "Client not found"}
    result = await ClientController.find_all()

    assert result == expected
