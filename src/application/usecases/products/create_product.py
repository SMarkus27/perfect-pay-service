from src.application.usecases.dtos.product import ProductDto
from src.domain.entities.product import Product
from src.infra.repositories.product import ProductRepository


class CreateProduct:

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product: ProductDto):
        valid_product = Product(**product).__dict__
        product_name = valid_product["name"]
        product_result = await self.product_repository.find_one_by_name(product_name)

        if len(product_result) > 0:
            return {
                "success": False,
                "message": "Product already exist",
            }

        result = await self.product_repository.create(valid_product)

        return {
            "success": True,
            "message": "product created successfully",
            "data": result,
        }
