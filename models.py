
class Request:
    from1 =  "склад",
    to = "магазин",
    amount = 3,
    product = "печеньки"

    def __init__(self, from1, to, amount, product):
        self.from1 = from1
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from1} в {self.to}"
