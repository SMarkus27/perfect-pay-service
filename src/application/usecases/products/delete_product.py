from src.infra.repositories.product import ProductRepository


class DeleteProduct:

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_id: int):
        result = await self.product_repository.find_one_by_id(product_id)

        if len(result) == 0:
            return {
                "success": False,
                "message": "Product not found"
            }

        await self.product_repository.delete(product_id)
        return {"success": True, "message": "Product deleted successfully"}
