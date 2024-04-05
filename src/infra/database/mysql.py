from decouple import config
from mysql.connector.aio import connect


class MySQLConnection:
    mysql_conn = None

    @classmethod
    def get_client(cls):
        try:
            cls.mysql_conn = connect(
                host=config("MYSQL_HOST"),
                port=int(config("MYSQL_PORT")),
                user=config("MYSQL_USER"),
                password=config("MYSQL_PASSWORD"),
                database=config("MYSQL_DATABASE_NAME"),
            )
            return cls.mysql_conn
        except Exception as e:
            raise Exception(e)
