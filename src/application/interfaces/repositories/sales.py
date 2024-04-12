from abc import ABCMeta, abstractmethod

from src.domain.entities.sales import Sales


class ISalesRepository(metaclass=ABCMeta):

    @abstractmethod
    async def create(self, sales: Sales) -> Sales:
        pass

    @abstractmethod
    async def find(self) -> list[Sales]:
        pass

    @abstractmethod
    async def find_one_by_id(self, sales_id: str) -> Sales:
        pass

    @abstractmethod
    async def update(self, sales_id: str, sales: Sales) -> Sales:
        pass

    @abstractmethod
    async def delete(self, sales_id: str) -> None:
        pass
