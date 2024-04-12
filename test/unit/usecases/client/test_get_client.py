from unittest.mock import patch, Mock

import pytest

from src.application.usecases.client.get_client import GetClient
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_get_client(find_one_by_id_patch: Mock):
    client_repository = ClientRepository()
    client_id = 1
    client = [
        {
            "name": "John Doe",
            "cpf": "10134578963",
            "email": "test@test.br",
            "id": client_id
        },
    ]
    find_one_by_id_patch.return_value = client

    expected = {"success": True, "data": client}

    result = await GetClient(client_repository).execute(client_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_get_client_client_not_found(find_one_by_id_patch: Mock):
    client_repository = ClientRepository()
    client_id = 100

    find_one_by_id_patch.return_value = []

    expected = {"success": False, "message": "Client not found"}

    result = await GetClient(client_repository).execute(client_id)

    assert result == expected
