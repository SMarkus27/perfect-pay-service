from src.application.usecases.dtos.sales import SalesDto
from src.domain.entities.sales import Sales
from src.infra.repositories.client import ClientRepository
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


class UpdateSales:
    def __init__(self, sales_repository: SalesRepository, client_repository: ClientRepository, product_repository: ProductRepository):
        self.sales_repository = sales_repository
        self.client_repository = client_repository
        self.product_repository = product_repository

    async def execute(self, sales_id: int, sales: SalesDto):
        client_result = await self.client_repository.find_one_by_id(sales["client"])

        if len(client_result) == 0:
            return {"success": False, "message": "Client not found"}

        product_result = await self.product_repository.find_one_by_id(sales["product"])

        if len(product_result) == 0:
            return {"success": False, "message": "Product not found"}

        result = await self.sales_repository.find_one_by_id(sales_id)

        if len(result) == 0:
            return {"success": False, "message": "Sales not found"}

        valid_sales = Sales(**sales).__dict__
        result = await self.sales_repository.update(sales_id, valid_sales)
        return {"success": True, "message": "Sales updated", "data": result}
