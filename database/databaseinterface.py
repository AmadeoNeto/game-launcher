from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self, path):
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: tuple = ()) -> tuple:
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: tuple = ()) -> list[tuple]:
        pass

    @abstractmethod
    def execute(self, query: str, params: tuple = ()) -> int:
        pass

    @abstractmethod
    def close(self):
        pass
