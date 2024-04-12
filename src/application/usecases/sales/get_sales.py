from src.infra.repositories.sales import SalesRepository


class GetSales:

    def __init__(self, sales_repository: SalesRepository):
        self.sales_repository = sales_repository

    async def execute(self, sales_id: int):
        result = await self.sales_repository.find_one_by_id(sales_id)

        if len(result) == 0:
            return {"success": False, "message": "Sales not found"}
        return {
            "success": True,
            "data": result,
        }
