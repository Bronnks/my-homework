# Итератор должен вывести все карты в виде строки
# “{название масти} {ранг}”.
class CardDeck:
 def __init__(self):
 self.length = 52
 self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
 self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

 def __next__(self):
     pass

 def __iter__(self):
     pass


deck = CardDeck()
while True:
    print(next(deck))
