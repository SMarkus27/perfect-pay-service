from src.infra.repositories.sales import SalesRepository


class GetAllSales:
    def __init__(self, sales_repository: SalesRepository):
        self.sales_repository = sales_repository

    async def execute(self):
        result = await self.sales_repository.find()

        if len(result) == 0:
            return {"success": False, "message": "Sales not found"}

        return {
            "success": True,
            "data": result,
        }
