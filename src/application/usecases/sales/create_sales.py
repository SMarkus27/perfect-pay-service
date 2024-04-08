from src.application.usecases.dtos.sales import SalesDto
from src.domain.entities.sales import Sales
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


class CreateSales:

    def __init__(
        self, sales_repository: SalesRepository, product_repository: ProductRepository
    ):
        self.sales_repository = sales_repository
        self.product_repository = product_repository

    async def execute(self, sales: SalesDto):
        valid_sales = Sales(**sales).__dict__

        product_id = valid_sales["product"]
        product_result = await self.product_repository.find_one_by_id(product_id)

        if len(product_result) == 0:
            return {
                "success": False,
                "message": "Product not found",
            }

        result = await self.sales_repository.create(valid_sales)

        return {
            "success": True,
            "message": "sales created successfully",
            "data": result,
        }
