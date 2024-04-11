# Third-Party library
import pytest

from src.controllers.client import ClientController


@pytest.mark.asyncio
async def test_create_client() -> None:
    new_client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test@test.br",
    }
    result = await ClientController.create(new_client)
    data = result.get("data")[0]
    assert int(data.get("id")) >= 0


@pytest.mark.asyncio
async def test_create_client_already_exist() -> None:
    new_client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test@test.br",
    }

    expected = {"success": False, "message": "Client already exists"}
    result = await ClientController.create(new_client)

    assert result == expected
