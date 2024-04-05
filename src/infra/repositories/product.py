from src.application.usecases.dtos.product import ProductDto
from src.infra.database.mysql import MySQLConnection


class ProductRepository:

    @classmethod
    async def execute_query(cls, query: str, transaction=False):
        client = await MySQLConnection.get_client()
        try:
            cursor = await client.cursor(dictionary=True)
            await cursor.execute(query)
            result = await cursor.fetchall()
            if transaction:
                await client.commit()

            await cursor.close()
            await client.close()

            return result
        except Exception as e:
            raise Exception(e)

    @classmethod
    async def create(cls, product: dict):
        query = (f"INSERT INTO products (name, description, price) "
                 f"VALUES ('{product['name']}','{product['description']}',{product['price']})")
        return await cls.execute_query(query, True)

    @classmethod
    async def find_one_by_id(cls, product_id: int):
        query = f"SELECT * FROM products WHERE id = '{product_id}'"
        result = await cls.execute_query(query)
        return result

    @classmethod
    async def find_one_by_name(cls, product_name: str):
        query = f"SELECT id FROM products WHERE name = '{product_name}'"
        result = await cls.execute_query(query)
        return result

    @classmethod
    async def find(cls):
        query = "SELECT * FROM products"
        result = await cls.execute_query(query)
        return result

    @classmethod
    async def update(cls, product_id: int, product: ProductDto):
        query = (f"UPDATE products SET name='{product['name']}',"
                 f"description='{product['description']}',"
                 f"price={product['price']} "
                 f"WHERE id={product_id}"
                 )
        result = await cls.execute_query(query, True)
        return result

    @classmethod
    async def delete(cls, product_id: int):
        query = f"DELETE FROM products WHERE id ='{product_id}'"
        result = await cls.execute_query(query, True)
        return result
