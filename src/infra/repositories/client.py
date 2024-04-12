from src.application.interfaces.repositories.client import IClientRepository
from src.application.usecases.dtos.client import ClientDto
from src.infra.database.postgres import PostgresSQLConnection


class ClientRepository(IClientRepository):

    @classmethod
    async def create(cls, client: dict):
        query = (
            f"INSERT INTO client (name, email, cpf) "
            f"VALUES ('{client['name']}','{client['email']}','{client['cpf']}') RETURNING *"
        )
        return await PostgresSQLConnection.execute_query(query, True)

    @classmethod
    async def find_one_by_id(cls, client_id: int):
        query = f"SELECT * FROM client WHERE id = '{client_id}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find_one_by_email(cls, email: str):
        query = f"SELECT id FROM client WHERE email = '{email}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find(cls):
        query = "SELECT * FROM client"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def update(cls, client_id: int, client: ClientDto):
        query = (
            f"UPDATE client SET name='{client['name']}',"
            f"cpf='{client['cpf']}',"
            f"email='{client['email']}' "
            f"WHERE id={client_id} RETURNING *"
        )
        result = await PostgresSQLConnection.execute_query(query, True)
        return result

    @classmethod
    async def delete(cls, client_id: int):
        query = f"DELETE FROM client WHERE id ='{client_id}' RETURNING *"
        result = await PostgresSQLConnection.execute_query(query, True)
        return result
