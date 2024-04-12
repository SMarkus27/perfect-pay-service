from unittest.mock import patch, Mock

import pytest

from src.application.usecases.client.get_all_client import GetAllClient
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "find")
async def test_get_all_client(find_patch: Mock):
    client_repository = ClientRepository()
    client = [
        {
            "name": "John Doe",
            "cpf": "10134578963",
            "email": "test@test.br",
        },
        {
            "name": "Jane Doe",
            "cpf": "10134500596",
            "email": "jane@test.br",
        },
    ]

    find_patch.return_value = client

    expected = {"success": True, "data": client}

    result = await GetAllClient(client_repository).execute()

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find")
async def test_get_all_client_client_not_found(find_patch: Mock):
    client_repository = ClientRepository()

    find_patch.return_value = []

    expected = {"success": False, "message": "Client not found"}

    result = await GetAllClient(client_repository).execute()

    assert result == expected
