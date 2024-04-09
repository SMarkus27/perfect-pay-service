from src.application.usecases.dtos.client import ClientDto
from src.application.usecases.client.create_client import CreateClient
from src.application.usecases.client.delete_client import DeleteClient
from src.application.usecases.client.get_all_client import GetAllClient
from src.application.usecases.client.get_client import GetClient
from src.application.usecases.client.update_client import UpdateClient
from src.infra.repositories.client import ClientRepository


class ClientController:

    @classmethod
    async def create(cls, client: ClientDto):
        client_repository = ClientRepository()
        return await CreateClient(client_repository).execute(client)

    @classmethod
    async def find_one(cls, client_id: int):
        client_repository = ClientRepository()
        return await GetClient(client_repository).execute(client_id)

    @classmethod
    async def find_all(cls):
        client_repository = ClientRepository()
        return await GetAllClient(client_repository).execute()

    @classmethod
    async def update(cls, client_id: int, client: ClientDto):
        client_repository = ClientRepository()
        return await UpdateClient(client_repository).execute(client_id, client)

    @classmethod
    async def delete(cls, client_id: int):
        client_repository = ClientRepository()
        return await DeleteClient(client_repository).execute(client_id)
