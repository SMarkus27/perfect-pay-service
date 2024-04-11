from src.application.usecases.dtos.client import ClientDto
from src.domain.entities.client import Client
from src.infra.repositories.client import ClientRepository


class CreateClient:

    def __init__(
        self, client_repository: ClientRepository
    ):
        self.client_repository = client_repository

    async def execute(self, client: ClientDto):
        valid_client = Client(**client).__dict__

        client_id = valid_client["email"]
        client_result = await self.client_repository.find_one_by_email(client_id)
        if len(client_result) > 0:
            return {
                "success": False,
                "message": "Client already exists",
            }

        result = await self.client_repository.create(valid_client)

        return {
            "success": True,
            "message": "client created successfully",
            "data": result,
        }
