from unittest.mock import patch, Mock

import pytest

from src.application.usecases.client.update_client import UpdateClient
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "update")
@patch.object(ClientRepository, "find_one_by_id")
async def test_update_client(find_one_by_id_patch: Mock, update_patch: Mock):
    client_repository = ClientRepository()
    client_id = 1

    new_client = {
        "name": "John Doee",
        "cpf": "10134578963",
        "email": "test@test.br",
    }
    find_one_by_id_patch.return_value = new_client

    expected = {"success": True, "message": "Client updated", "data": new_client}
    update_patch.return_value = new_client
    result = await UpdateClient(client_repository).execute(client_id, new_client)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_update_client_client_not_found(find_one_by_id_patch: Mock):
    client_repository = ClientRepository()
    client_id = 100

    new_client = (
        {
            "product": 2,
            "client_date": "2024-02-03",
            "quantity": 50,
            "discount": 0.65,
            "status": True
        },
    )

    find_one_by_id_patch.return_value = []

    expected = {"success": False, "message": "Client not found"}

    result = await UpdateClient(client_repository).execute(client_id, new_client)

    assert result == expected
