from src.application.interfaces.repositories.products import IProductsRepository
from src.application.usecases.dtos.product import ProductDto
from src.domain.entities.product import Product
from src.infra.database.postgres import PostgresSQLConnection


class ProductRepository(IProductsRepository):

    @classmethod
    async def create(cls, product: dict) -> Product:
        query = (
            f"INSERT INTO products (name, description, price) "
            f"VALUES ('{product['name']}','{product['description']}',{product['price']}) RETURNING *"
        )
        return await PostgresSQLConnection.execute_query(query, True)

    @classmethod
    async def find_one_by_id(cls, product_id: int) -> list[Product]:
        query = f"SELECT * FROM products WHERE id = '{product_id}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find_one_by_name(cls, product_name: str) -> Product:
        query = f"SELECT id FROM products WHERE name = '{product_name}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find(cls) -> Product:
        query = "SELECT * FROM products"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def update(cls, product_id: int, product: ProductDto):
        query = (
            f"UPDATE products SET name='{product['name']}',"
            f"description='{product['description']}',"
            f"price={product['price']} "
            f"WHERE id={product_id} RETURNING *"
        )
        result = await PostgresSQLConnection.execute_query(query, True)
        return result

    @classmethod
    async def delete(cls, product_id: int):
        query = f"DELETE FROM products WHERE id ='{product_id}' RETURNING *"
        result = await PostgresSQLConnection.execute_query(query, True)
        return result
