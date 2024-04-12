# Third-Party library
import pytest

from src.controllers.client import ClientController


@pytest.mark.asyncio
async def test_find_one_client() -> None:
    client_id = 1
    result = await ClientController.find_one(client_id)
    assert len(result.get("data")) == 1


@pytest.mark.asyncio
async def test_find_client_client_not_found() -> None:
    client_id = 10

    expected = {"success": False, "message": "Client not found"}
    result = await ClientController.find_one(client_id)

    assert result == expected
