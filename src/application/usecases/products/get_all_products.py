from src.infra.repositories.product import ProductRepository


class GetAllProducts:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self):
        result = await self.product_repository.find()

        if len(result) == 0:
            return {"success": False, "message": "Products not found"}

        return {
            "success": True,
            "data": result,
        }
