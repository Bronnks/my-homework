def create_dict_drinks():
    n = int(input('Введите количество напитков - '))
    dct = {input('Введите название напитка - '): int(input('Введите стоимость напитка - ')) for _ in range(n)}
    return dct


def vending_machine(dct):
    print('В меню представлены следующие напитки:')
    for k, v in dct.items():
        print(f'{k} - {v} рублей.')

    for _ in range(len(dct)):
        drink = (yield str)
        if drink not in drinks:
            print('Такого напитка нету в меню.')
        else:
            print(f'Вы выбрали {drink}. Внесите {drinks[drink]} рублей.')
        pay = (yield int)
        if pay >= dct[drink]:
            print(f'Ваша сдача составляет - {pay - dct[drink]} рублей.')
        else:
            print('Недостаточно денег.')


drinks = create_dict_drinks()
vm = vending_machine(drinks)
next(vm)
vm.send(input('Выберите напиток - '))
vm.send(int(input('Внесите плату - ')))
