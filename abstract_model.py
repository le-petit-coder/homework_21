
from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, item: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, item: str, quantity: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
