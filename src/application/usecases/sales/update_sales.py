from src.application.usecases.dtos.sales import SalesDto
from src.domain.entities.sales import Sales
from src.infra.repositories.sales import SalesRepository


class UpdateSales:
    def __init__(self, sales_repository: SalesRepository):
        self.sales_repository = sales_repository

    async def execute(self, sales_id: int, sales: SalesDto):
        result = await self.sales_repository.find_one_by_id(sales_id)
        if len(result) == 0:
            return {"success": False, "message": "Sales not found"}

        valid_sales = Sales(**sales).__dict__
        result = await self.sales_repository.update(sales_id, valid_sales)
        return {"success": True, "message": "Sales updated", "data": result}
