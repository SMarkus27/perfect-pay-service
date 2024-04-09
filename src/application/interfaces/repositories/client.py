from abc import ABCMeta, abstractmethod

from src.domain.entities.client import Client


class IClientRepository(metaclass=ABCMeta):

    @abstractmethod
    async def create(self, client: Client) -> Client:
        pass

    @abstractmethod
    async def find(self) -> list[Client]:
        pass

    @abstractmethod
    async def find_one_by_id(self, client_id: str) -> Client:
        pass

    @abstractmethod
    async def update(self, client_id: str, client: Client) -> Client:
        pass

    @abstractmethod
    async def delete(self, client_id: str) -> None:
        pass
