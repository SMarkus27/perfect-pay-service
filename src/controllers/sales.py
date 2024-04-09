from src.application.usecases.dtos.sales import SalesDto
from src.application.usecases.sales.create_sales import CreateSales
from src.application.usecases.sales.delete_sales import DeleteSales
from src.application.usecases.sales.get_all_sales import GetAllSales
from src.application.usecases.sales.get_sales import GetSales
from src.application.usecases.sales.update_sales import UpdateSales
from src.infra.repositories.client import ClientRepository
from src.infra.repositories.product import ProductRepository
from src.infra.repositories.sales import SalesRepository


class SalesController:

    @classmethod
    async def create(cls, sale: SalesDto):
        sale_repository = SalesRepository()
        product_repository = ProductRepository()
        client_repository = ClientRepository()

        return await CreateSales(sale_repository, product_repository, client_repository).execute(sale)

    @classmethod
    async def find_one(cls, sale_id: int):
        sale_repository = SalesRepository()
        return await GetSales(sale_repository).execute(sale_id)

    @classmethod
    async def find_all(cls):
        sale_repository = SalesRepository()
        return await GetAllSales(sale_repository).execute()

    @classmethod
    async def update(cls, sale_id: int, sale: SalesDto):
        sale_repository = SalesRepository()
        return await UpdateSales(sale_repository).execute(sale_id, sale)

    @classmethod
    async def delete(cls, sale_id: int):
        sale_repository = SalesRepository()
        return await DeleteSales(sale_repository).execute(sale_id)
