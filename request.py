from abstract_model import AbstractStorage
from typing import Dict, List

from errors import UnknownStorage, WrongRequest


class Request:

    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        request_split: List[str] = request.strip().lower().split(' ')

        if len(request_split) != 7:
            raise WrongRequest

        self.quantity = int(request_split[1])
        self.product = request_split[2]
        self.departure = request_split[4]
        self.destination = request_split[6]

        if self.destination not in storages or self.departure not in storages:
            raise UnknownStorage
