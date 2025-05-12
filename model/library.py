import sqlite3

from model.game import Game
from utils.path_utils import PathUtils
from database.databaseinterface import DatabaseInterface

# TODO: handle SQL exceptions


class Library:
    def __init__(self, dabase_handler: DatabaseInterface):
        self.__library_db = dabase_handler
        self.__connect_db()
        self.__try_create_table()

    def __connect_db(self) -> sqlite3.Connection:
        PathUtils.try_create_data_dir()
        library_db_path = PathUtils.get_library_db_path()
        return self.__library_db.connect(library_db_path)

    def __try_create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS library (
            game_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            path TEXT UNIQUE,
            cover_art_path TEXT,
            hours_played REAL,
            last_played TIMESTAMP
        );
        """
        self.__library_db.execute(create_table_sql)

    def get_all_games(self) -> list[Game]:
        select_game_sql = """
        SELECT game_id, title, path, cover_art_path, hours_played, last_played
        FROM library;
        """
        rows = self.__library_db.fetch_all(select_game_sql)

        return [Game(*row) for row in rows]

    def get_game_by_title(self, title: str) -> Game | None:
        select_game_sql = """
        SELECT game_id, title, path, cover_art_path, hours_played, last_played
        FROM library WHERE title = (?);
        """
        row = self.__library_db.fetch_one(select_game_sql, (title,))
        result = Game(*row) if row is not None else None
        return result

    def add_game(self, title, path, cover_art_path) -> bool:
        insert_game_sql = f"""
        INSERT INTO library (title, path, cover_art_path)
        VALUES (?, ?, ?);
        """
        rows_affected = self.__library_db.execute(insert_game_sql,
                                                  (title, path, cover_art_path))
        return rows_affected > 0

    def remove_game_by_title(self, title: str) -> bool:
        if not title:
            return False

        delete_game_sql = "DELETE FROM library WHERE title = (?);"
        rows_affected = self.__library_db.execute(delete_game_sql, (title,))
        return rows_affected > 0
