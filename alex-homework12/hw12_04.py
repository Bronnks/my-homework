class BankAccount:
    def __init__(self, number: int, balance: int, owner: object):
        self.number = number
        self.balance = balance
        self.owner = owner

    def deposit(self, value: int):
        self.balance += value
        print(f'Вы успешно пополнили счет на {value}.')

    def withdraw(self, value: int):
        if self.balance >= value:
            self.balance -= value
            print(f'Вы успешно сняли {value}.')
        else:
            print('Недостаточно средств для снятия.')

    def transfer(self, num: int, value: int):                           # Перевод с текущего счета на выбранный
        if len(self.owner.accounts) == 1:                               # где num - номер счета для перевода
            print('У данного пользователя только один счет, текущий.')  # value - сумма перевода
        else:
            no_transfer = True
            for i in self.owner.accounts:
                if i.number == num:
                    no_transfer = False
                    if self.balance >= value:
                        self.balance -= value
                        i.balance += value
                    else:
                        print('Недостаточно средств для перевода.')
            if no_transfer:
                print('Cчет с таким номером не принадлежит данному пользователю.')


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.accounts = []

    def add_acc(self, acc: object):
        self.accounts.append(acc)

    def get_total_balance(self, details: bool = False):
        if details:
            count = 0
            for i in self.accounts:
                count = i.balance
                print(f'На счету {i.number} лежит {i.balance} рублей.')
            print(f'Общая сумма на всех счетах: {count}')

        else:
            res = sum(i.balance for i in self.accounts)
            print(f'Общая сумма на всех счетах: {res}')
