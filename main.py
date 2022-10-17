from abstract_model import AbstractStorage
from base_shop import Shop
from base_store import Store
from typing import Dict

from errors import BaseError
from request import Request
from courier import Courier

store = Store(
    items={
        "торт": 20,
        "печенька": 15
    },
    capacity=100
)

shop = Shop(
    items={
        "торт": 5
    },
    capacity=20,
    max_capacity=5
)

storages: Dict[str, AbstractStorage] = {
    "склад": store,
    "магазин": shop
}


def main():
    print("Добрый день!\n")

    while True:
        for storage_name, storage in storages.items():
            print(f"В {storage_name} хранится {storage.get_items()}")

        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Если захотите закончить заказ, введите "stop" или "стоп"\n')
        if user_input in ["stop", "стоп"]:
            break
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(request=request, storages=storages)
        courier.move()


if __name__ == '__main__':
    main()