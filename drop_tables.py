from asyncio import run

from src.infra.database.postgres import PostgresSQLConnection


async def delete_table():
    connection = await PostgresSQLConnection.get_client()
    cursor = connection.cursor()
    await cursor.execute("DROP TABLE products CASCADE ")
    await cursor.execute("DROP TABLE sales")
    await cursor.execute("DROP TABLE client CASCADE")
    await connection.commit()
    await cursor.close()
    print("Drop tables completed")


if __name__ == "__main__":
    run(delete_table())
