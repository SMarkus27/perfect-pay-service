from decouple import config
from psycopg import AsyncConnection
from psycopg.rows import dict_row


class PostgresSQLConnection:
    postgres_conn = None

    @classmethod
    def get_client(cls):
        try:
            cls.postgres_conn = AsyncConnection.connect(host=config("POSTGRES_HOST"),
                                      dbname=config("POSTGRES_DB"),
                                      user=config("POSTGRES_USER"),
                                      password=config("POSTGRES_PASSWORD"),
                                      row_factory=dict_row)
            return cls.postgres_conn
        except Exception as e:
            raise Exception(e)
