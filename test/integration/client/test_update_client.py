# Third-Party library
import pytest

from src.controllers.client import ClientController


@pytest.mark.asyncio
async def test_update_client() -> None:
    old_client = {
        "name": "Jane Lore",
        "cpf": "10134578963",
        "email": "jane@lore.br",
    }

    client = await ClientController.create(old_client)
    data = client.get("data")[0]
    client_id = data.get("id")

    new_client = {
        "name": "Jane Jane",
        "cpf": "10134578963",
        "email": "jane@lore.br",
    }

    result = await ClientController.update(client_id, new_client)

    assert result.get("data")[0] != old_client


@pytest.mark.asyncio
async def test_find_client_client_not_found() -> None:
    client_id = 100

    expected = {"success": False, "message": "Client not found"}
    new_client = {
        "client": 1,
        "client_date": "2024-02-02",
        "quantity": 5,
        "discount": 0.5,
        "status": True
    }

    result = await ClientController.update(client_id, new_client)

    assert result == expected
