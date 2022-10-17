from base_storage import Storage
from typing import Dict
from errors import TooManyDifferentProductsError


class Shop(Storage):

    def __init__(self, items: Dict[str, int], capacity: int, max_capacity: int):
        self.max_capacity = max_capacity
        super().__init__(items, capacity)

    def add(self, item: str, capacity: int):
        if self.get_unique_items_count() >= self.max_capacity:
            raise TooManyDifferentProductsError
        super().add(item, capacity)

