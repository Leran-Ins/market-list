from __main__ import Reminder


class Item:
    def __init__(self, name: str, price: float, reminder: Reminder, position: int):
        self.name = name
        self.price = price
        self.reminder_text = reminder.text
        self.position = position
