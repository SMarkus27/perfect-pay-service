from abc import ABCMeta, abstractmethod

from src.domain.entities.product import Product


class IProductsRepository(metaclass=ABCMeta):

    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def find(self) -> list[Product]:
        pass

    @abstractmethod
    async def find_one_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    async def update(self, product_id: str, product: Product) -> Product:
        pass

    @abstractmethod
    async def delete(self, product_id: str) -> None:
        pass
