class Message:
    __choice = '(y/n)'
    ITEM_NAME = 'Que item você quer colocar na lista? '
    ITEM_PRICE = 'Qual seria o preço estimado para o item? '
    BLANK_NAME = 'O nome do item não pode ser apenas de espaços! Tente de novo.'
    EMPTY_NAME = 'O nome do item não pode ser vazio! Tente de novo.'
    ADD_REMINDER = 'Deseja adicionar um lembrete? {} '.format(__choice)
    ANOTHER_ITEM = 'Adicionar outro item? {} '.format(__choice)
    ADDED_ITEM = '{}: adicionado \'{}\' com o preço estimado de \'{}\' lembrete: \'{}\''
    EXPENSIVE_ITEM = 'O item mais caro saiu por {}'
    CHEAPER_ITEM = 'O item mais barato saiu por {}'
