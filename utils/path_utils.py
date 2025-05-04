import os
import sys
from utils.constants import APPLICATION_NAME


class PathUtils:

    @staticmethod
    def get_data_path() -> str:
        if sys.platform == "win32":  # Windows
            base_dir = os.getenv('APPDATA')
        elif sys.platform == "darwin":  # MACOS
            base_dir = os.path.expanduser("~/Library/Application Support")
        else:  # Assume Linux
            base_dir = os.path.expanduser("~/.local/share")

        data_path = os.path.join(base_dir, APPLICATION_NAME)
        return data_path

    @staticmethod
    def try_create_data_dir():
        data_path = PathUtils.get_data_path()
        os.makedirs(data_path, exist_ok=True)

    @staticmethod
    def get_library_db_path() -> str:
        library_db_path = os.path.join(PathUtils.get_data_path(), "library.db")
        return library_db_path
