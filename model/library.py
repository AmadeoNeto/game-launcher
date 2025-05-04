from dataclasses import dataclass
from typing import List
from model.game import Game
from utils.path_utils import PathUtils
import sqlite3


class Library:
    def __init__(self):
        self.__library_db = self.__get_db_connection()
        self.__try_create_table()

    def __get_db_connection(self) -> sqlite3.Connection:
        PathUtils.try_create_data_dir()
        library_db_path = PathUtils.get_library_db_path()
        return sqlite3.connect(library_db_path, detect_types=sqlite3.PARSE_DECLTYPES)

    def __try_create_table(self):
        with self.__library_db as conn:
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
            conn.execute(create_table_sql)

    def get_all_games(self) -> List[Game]:
        with self.__library_db as conn:
            select_game_sql = """
            SELECT game_id, title, path, cover_art_path, hours_played, last_played
            FROM library;
            """
            rows = conn.execute(select_game_sql).fetchall()

            return [Game(*row) for row in rows]

    def get_game_by_title(self, title: str) -> Game | None:
        with self.__library_db as conn:
            select_game_sql = """
            SELECT game_id, title, path, cover_art_path, hours_played, last_played
            FROM library WHERE title = (?);
            """
            row = conn.execute(select_game_sql, (title,)).fetchone()
            result = Game(*row) if row is not None else None
            return result

    def add_game(self, title, path, cover_art_path) -> bool:
        with self.__library_db as conn:
            insert_game_sql = f"""
            INSERT INTO library (title, path, cover_art_path)
            VALUES (?, ?, ?);
            """
            cursor = conn.execute(insert_game_sql,
                                  (title, path, cover_art_path))
            return cursor.rowcount > 0

    def remove_game_by_title(self, title: str) -> bool:
        if not title:
            return False
        with self.__library_db as conn:
            delete_game_sql = "DELETE FROM library WHERE title = (?);"
            cursor = conn.execute(delete_game_sql, (title,))
            return cursor.rowcount > 0
