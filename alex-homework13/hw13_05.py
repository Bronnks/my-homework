from abc import ABC, abstractmethod


class Order:
    def __init__(self, items: str, total: int) -> None:
        self.items = items
        self.total = total

    def process(self, database_storage) -> None:
        database_storage.save(self)


class Storage(ABC):
    @abstractmethod
    def save(self, item: Order) -> None:
        pass


class Database(Storage):
    @staticmethod
    def connect() -> None:
        print('Connect to the Database.')

    def save(self, item_object: Order) -> None:
        print(f'Save {item_object} to the Database storage.')


class File(Storage):
    def save(self, item_object: Order) -> None:
        print(f'Save {item_object} to the file.')
