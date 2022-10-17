from typing import Dict
from abstract_model import AbstractStorage
from errors import NotEnoughSpaceError, NotEnoughProductError, ProductUnknownError


class Storage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def __repr__(self):
        pass

    def add(self, item, quantity) -> None:
        if self.get_free_space() < quantity:
            raise NotEnoughSpaceError
        if item in self.__items:
            self.__items[item] += quantity
        else:
            self.__items = quantity

    def remove(self, item, quantity):
        if item not in self.__items:
            raise ProductUnknownError
        if self.__items[item] < 0:
            raise NotEnoughProductError
        self.__items[item] -= quantity
        if self.__items[item] == 0:
            self.__items.pop(item)

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)