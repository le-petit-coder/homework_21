from request import Request
from abstract_model import AbstractStorage
from typing import Dict


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.request = request
        self.departure: AbstractStorage = storages[self.request.departure]
        self.destination: AbstractStorage = storages[self.request.destination]

    def move(self):
        self.departure.remove(item=self.request.product, quantity=self.request.quantity)
        print(f"Курьер забирает {self.request.quantity} {self.request.product} из {self.request.departure}")
        self.destination.add(item=self.request.product, quantity=self.request.quantity)
        print(f"Курьер доставил {self.request.quantity} {self.request.product} в {self.request.destination}")