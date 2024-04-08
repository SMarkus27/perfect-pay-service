from src.application.interfaces.repositories.sales import ISalesRepository
from src.application.usecases.dtos.sales import SalesDto
from src.infra.database.postgres import PostgresSQLConnection


class SalesRepository(ISalesRepository):

    @classmethod
    async def create(cls, sales: dict):
        query = (
            f"INSERT INTO sales (product, sales_date, quantity, discount, status) "
            f"VALUES ({sales['product']},'{sales['sales_date']}',{sales['quantity']},{sales['discount']}, {sales['status']}) RETURNING *"
        )
        return await PostgresSQLConnection.execute_query(query, True)

    @classmethod
    async def find_one_by_id(cls, sales_id: int):
        query = f"SELECT * FROM sales WHERE id = '{sales_id}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find(cls):
        query = "SELECT * FROM sales"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def update(cls, sales_id: int, sales: SalesDto):
        query = (
            f"UPDATE sales SET sales_date='{sales['sales_date']}',"
            f"quantity={sales['quantity']},"
            f"discount={sales['discount']},"
            f"status={sales['status']} "
            f"WHERE id={sales_id} RETURNING *"
        )
        result = await PostgresSQLConnection.execute_query(query, True)
        return result

    @classmethod
    async def delete(cls, sales_id: int):
        query = f"DELETE FROM sales WHERE id ='{sales_id}' RETURNING *"
        result = await PostgresSQLConnection.execute_query(query, True)
        return result
