from asyncio import run


from src.infra.database.postgres import PostgresSQLConnection


async def create_tables():
    connection = await PostgresSQLConnection.get_client()
    cursor = connection.cursor()
    product_query = ("CREATE TABLE IF NOT EXISTS products(id serial  PRIMARY KEY, name VARCHAR(50), description VARCHAR(50), price decimal(5,2)); "
                     "CREATE TABLE IF NOT EXISTS client(id serial  PRIMARY KEY, name varchar(50), email varchar(40), cpf varchar(11));"
                     "CREATE TABLE IF NOT EXISTS sales(id serial  PRIMARY KEY, product int references products(id), client int references client(id), sales_date DATE, quantity int, discount decimal(2,2), status bool)")
    await cursor.execute(product_query)

    await connection.commit()
    await cursor.close()
    await connection.close()
    print("Tables created")

if __name__ == "__main__":
    run(create_tables())


# "nicoulaj"