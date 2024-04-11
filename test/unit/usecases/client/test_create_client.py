from unittest.mock import patch, Mock

import pytest

from src.application.usecases.client.create_client import CreateClient
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "create")
@patch.object(ClientRepository, "find_one_by_email")
async def test_create_client(find_one_by_email_patch: Mock, create_patch: Mock):
    client_repository = ClientRepository()

    client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test@test.br",
    }

    client_id = []

    find_one_by_email_patch.return_value = client_id

    client_with_id = client.copy()
    client_with_id["id"] = 1

    expected = {
        "success": True,
        "message": "client created successfully",
        "data": client_with_id,
    }

    create_patch.return_value = client_with_id
    result = await CreateClient(client_repository).execute(client)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_email")
async def test_create_client_client_already_exist(find_one_by_email_patch: Mock):
    client_repository = ClientRepository()

    client = {
        "name": "John Doe",
        "cpf": "10134578963",
        "email": "test@test.br",
    }

    client_id = [{"id": 1}]

    find_one_by_email_patch.return_value = client_id

    expected = {
        "success": False,
        "message": "Client already exists",
    }

    result = await CreateClient(client_repository).execute(client)

    assert result == expected
