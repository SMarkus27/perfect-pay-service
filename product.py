from asyncio import run


from src.infra.database.postgres import PostgresSQLConnection


async def create_product_table():
    connection = await PostgresSQLConnection.get_client()
    cursor = connection.cursor()
    await cursor.execute(
        "CREATE TABLE IF NOT EXISTS products(id serial  PRIMARY KEY, name VARCHAR(50), description VARCHAR(50), price decimal(5,2))"
    )
    await connection.commit()
    await cursor.close()
    await connection.close()


if __name__ == "__main__":
    run(create_product_table())