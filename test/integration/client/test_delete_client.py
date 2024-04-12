import pytest

from src.controllers.client import ClientController


@pytest.mark.asyncio
async def test_delete_client() -> None:
    new_client = {
        "name": "Jane Doe",
        "cpf": "10134578963",
        "email": "jane@test.br",
    }

    client = await ClientController.create(new_client)
    data = client.get("data")[0]
    client_id = data.get("id")
    expected = {"success": True, "message": "Client deleted successfully"}

    result = await ClientController.delete(client_id)

    assert result == expected


@pytest.mark.asyncio
async def test_delete_client_client_not_found() -> None:
    client_id = 100

    expected = {"success": False, "message": "Client not found"}
    result = await ClientController.delete(client_id)
    assert result == expected
