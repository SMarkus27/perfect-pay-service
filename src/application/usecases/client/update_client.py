from src.application.usecases.dtos.client import ClientDto
from src.domain.entities.client import Client
from src.infra.repositories.client import ClientRepository


class UpdateClient:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    async def execute(self, client_id: int, client: ClientDto):
        result = await self.client_repository.find_one_by_id(client_id)
        if len(result) == 0:
            return {"success": False, "message": "Client not found"}

        valid_client = Client(**client).__dict__
        result = await self.client_repository.update(client_id, valid_client)
        return {"success": True, "message": "Client updated", "data": result}
