from unittest.mock import patch, Mock

import pytest

from src.application.usecases.client.delete_client import DeleteClient
from src.infra.repositories.client import ClientRepository


@pytest.mark.asyncio
@patch.object(ClientRepository, "delete")
@patch.object(ClientRepository, "find_one_by_id")
async def test_delete_client(find_one_by_id_patch: Mock, delete_patch: Mock):
    client_repository = ClientRepository()
    client_id = 2

    find_one_by_id_patch.return_value = [{"id": client_id}]

    expected = {
        "success": True,
        "message": "Client deleted successfully",
    }

    result = await DeleteClient(client_repository).execute(client_id)

    assert result == expected


@pytest.mark.asyncio
@patch.object(ClientRepository, "find_one_by_id")
async def test_delete_client_client_not_found(find_one_by_id_patch: Mock):
    client_repository = ClientRepository()
    client_id = 100

    find_one_by_id_patch.return_value = []

    expected = {
        "success": False,
        "message": "Client not found",
    }

    result = await DeleteClient(client_repository).execute(client_id)

    assert result == expected
