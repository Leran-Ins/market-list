class Item:
    def __init__(self, name: str, price: float, amount: int, position: int):
        self.name = name
        self.price = price if price < 0.0 else price * float(amount)
        self.amount = amount
        self.position = position
