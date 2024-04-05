from abc import ABCMeta, abstractmethod

from src.domain.entities.product import Product


class IProductsRepository(metaclass=ABCMeta):

    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def get_all_products(self) -> list[Product]:
        pass

    @abstractmethod
    async def get_product(self, product_id: str) -> Product:
        pass

    @abstractmethod
    async def update_product(self, product_id: str, product: Product) -> Product:
        pass

    @abstractmethod
    async def delete_product(self, product_id: str) -> None:
        pass
