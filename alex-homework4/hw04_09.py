# Итератор должен вывести все карты в виде строки
# “{название масти} {ранг}”.
class CardDeck:
    def __init__(self):
        self.length = 52
        self.start2 = 0
        self.start = -2
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def __next__(self):

        if self.start2 < len(self.suits):
            self.start += 1
            if self.start < 12:
                return f'{self.suits[self.start2]} {self.ranks[self.start + 1]}'
            else:
                self.start = -1
                self.start2 += 1
                return f'{self.suits[self.start2]} {self.ranks[self.start + 1]}'
        else:
            raise StopIteration


def __iter__(self):
    return self


deck = CardDeck()
# чтобы не вызывать StopIteration использовал цикл for, т.к. мы знаем сколько карт нам надо отобразить
for i in range(52):
    print(next(deck))
