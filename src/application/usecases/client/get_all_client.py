from src.infra.repositories.client import ClientRepository


class GetAllClient:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    async def execute(self):
        result = await self.client_repository.find()

        if len(result) == 0:
            return {"success": False, "message": "Client not found"}

        return {
            "success": True,
            "data": result,
        }
