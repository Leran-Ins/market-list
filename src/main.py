from constant import Message
from item import Item


def manage_list():
    position = 0
    items = list()
    while True:
        name = input(Message.ITEM_NAME).lower().capitalize()
        if name_check(name):
            print(Message.INVALID_NAME.format(name))
            continue

        price = input(Message.ITEM_PRICE)
        if price.endswith('.'):
            price = price[:-1]

        amount = input(Message.ITEM_AMOUNT)
        if not amount.isnumeric():
            amount = 1

        amount = int(amount)
        if amount < 1:
            amount = 1

        position += 1
        item = Item(name, float(price), amount, position)
        items.append(item)

        another_item = input(Message.ANOTHER_ITEM)
        if not choice(another_item):
            break

    for item in items:
        print('\033[1;94m',
              Message.ADDED_ITEM.format(item.position, item.amount, item.name, item.price))

    prices = list(map(lambda x: x.price, items))
    prices.sort()
    print('\033[1;91m', Message.EXPENSIVE_ITEM.format(prices[-1]))
    print(f'\033[1;31m', Message.CHEAPER_ITEM.format(prices[0]))


def name_check(name: str) -> bool:
    blank = isblank(name)
    empty = is_empty(name)
    numeric = name.isnumeric()
    return blank or empty or numeric


def choice(value: str) -> bool:
    """Verifica um valor, True para 'y', False para qualquer outro valor"""
    option = False
    if is_empty(value) \
            or isblank(value):
        return option

    value = value[0]
    if value == 'y':
        option = True
    return option


def isblank(string: str) -> bool:
    """Verifica se uma 'string' possui apenas espaços em branco"""
    blank = False
    if not is_empty(string):
        spaces = whitespaces(string)
        blank = len(string) == spaces
    return blank


def is_empty(string: str) -> bool:
    """Verifica se uma 'string' é vazia"""
    return len(string) == 0


def whitespaces(string: str) -> int:
    """Número de espaços em branco em uma 'string'"""
    count = 0
    index = 0
    while index < len(string):
        char = string[index]
        if char.isspace():
            count += 1
        index += 1
    return count


manage_list()
