from src.infra.repositories.client import ClientRepository


class GetClient:

    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    async def execute(self, client_id: int):
        result = await self.client_repository.find_one_by_id(client_id)

        if len(result) == 0:
            return {"success": False, "message": "Client not found"}
        return {
            "success": True,
            "data": result,
        }
