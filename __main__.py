from constant import Message
from item import Item


class Reminder:
    def __init__(self, option: str):
        option = option.lower()
        text = 'Sem lembrete!'
        if choice(option):
            text = input('Qual é o lembrete? ')
        self.text = text


def manage_list():
    position = 0
    items = dict()
    while True:
        name = input(Message.ITEM_NAME)
        if isblank(name):
            print(Message.BLANK_NAME)
            continue

        if is_empty(name):
            print(Message.EMPTY_NAME)
            continue

        price = input(Message.ITEM_PRICE)
        if isblank(price) \
                or not price.isnumeric():
            price = '0.0'

        option = input(Message.ADD_REMINDER)
        reminder = Reminder(option)
        position += 1
        item = Item(name, float(price), reminder, position)
        items[str(position)] = item

        another_item_option = input(Message.ANOTHER_ITEM).lower()
        if not choice(another_item_option):
            break

    for key in items:
        item = items[key]
        print('\033[1;94m',
              Message.ADDED_ITEM.format(item.position, item.name, item.price, item.reminder_text))

    prices = list(map(lambda x: x.price, items.values()))
    prices.sort()
    print('\033[1;91m', Message.EXPENSIVE_ITEM.format(prices[-1]))
    print(f'\033[1;31m', Message.CHEAPER_ITEM.format(prices[0]))


def isblank(string: str) -> bool:
    blank = False
    if not is_empty(string):
        spaces = whitespaces(string)
        blank = len(string) == spaces
    return blank


def is_empty(string: str) -> bool:
    return string == ''


def whitespaces(string: str) -> int:
    count = 0
    index = 0
    while index < len(string):
        char = string[index]
        if char.isspace():
            count += 1
        index += 1
    return count


def choice(value: str) -> bool:
    option = False
    if is_empty(value):
        return option

    value = value[0]
    if value == 'y':
        option = True
    return option


manage_list()
