import psycopg2
import psycopg2.extras
from core.models import DBModel
from configs import DB_CONNECTION
from psycopg2._psycopg import connection, cursor


class DBManager:
    HOST = DB_CONNECTION["HOST"]
    USER = DB_CONNECTION["USER"]
    PORT = DB_CONNECTION["PORT"]
    PASSWORD = DB_CONNECTION["PASSWORD"]

    def __init__(self, database, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password

        self.conn: connection = \
            psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port, password=password)

    def __del__(self):
        self.conn.close()  # Close the connection on delete

    def __get_cursor(self) -> cursor:
        # Changing the fetch output from Tuple to Dict utilizing RealDictCursor cursor factory
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def create(self, model_instance: DBModel) -> int:
        """
            return id of created model instance from table
        """

    def read(self, model_class: type, pk) -> DBModel:  # get
        """
            returns an instance of the Model with inserted values
        """

    def update(self, model_instance: DBModel) -> None:
        """
            update instance in db table by get all model_instance attrs
        """

    def delete(self, model_instance: DBModel) -> None:
        """
            delete instance method
        """
