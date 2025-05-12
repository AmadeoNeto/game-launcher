import sqlite3

from database.databaseinterface import DatabaseInterface


class SQLiteHandler(DatabaseInterface):

    def __init__(self):
        self.connection = None

    def connect(self, path):
        self.connection = sqlite3.connect(
            path, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetch_one(self, query: str, params: tuple = ()) -> tuple:
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetch_all(self, query: str, params: tuple = ()) -> list[tuple]:
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def execute(self, query: str, params: tuple = ()) -> int:
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.rowcount

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
