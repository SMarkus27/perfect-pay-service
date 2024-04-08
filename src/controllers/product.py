from src.application.usecases.dtos.product import ProductDto
from src.application.usecases.products.create_product import CreateProduct
from src.application.usecases.products.delete_product import DeleteProduct
from src.application.usecases.products.get_all_products import GetAllProducts
from src.application.usecases.products.get_product import GetProduct
from src.application.usecases.products.update_product import UpdateProduct
from src.infra.repositories.product import ProductRepository


class ProductController:

    @classmethod
    async def create(cls, product: ProductDto):
        product_repository = ProductRepository()
        return await CreateProduct(product_repository).execute(product)

    @classmethod
    async def find_one(cls, product_id: int):
        product_repository = ProductRepository()
        return await GetProduct(product_repository).execute(product_id)

    @classmethod
    async def find_all(cls):
        product_repository = ProductRepository()
        return await GetAllProducts(product_repository).execute()

    @classmethod
    async def update(cls, product_id: int, product: ProductDto):
        product_repository = ProductRepository()
        return await UpdateProduct(product_repository).execute(product_id, product)

    @classmethod
    async def delete(cls, product_id: int):
        product_repository = ProductRepository()
        return await DeleteProduct(product_repository).execute(product_id)
