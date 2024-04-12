from src.application.usecases.dtos.product import ProductDto
from src.domain.entities.product import Product
from src.infra.repositories.product import ProductRepository


class UpdateProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_id: int, product: ProductDto):
        result = await self.product_repository.find_one_by_id(product_id)
        if len(result) == 0:
            return {"success": False, "message": "Product not found"}

        valid_product = Product(**product).__dict__
        result = await self.product_repository.update(product_id, valid_product)
        return {"success": True, "message": "Product updated", "data": result}
