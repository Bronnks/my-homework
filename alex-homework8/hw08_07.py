import pickle
from faker import Faker

fake = Faker()


class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return self.sound

    def say_name(self):
        return self.name

    def say_species(self):
        return self.species


def create_list():
    cat = Animal("Барсик", "кот", "мяу")
    dog = Animal("Шарик", "собака", "гав")
    horse = Animal("Зорька", "лошадь", "иго-го")
    fox = Animal("Рыжик", "лиса", "тыф-тыф")
    wolf = Animal("Серый", "волк", "аууу")
    return [cat, dog, horse, fox, wolf]


with open('animals.pickle', 'wb') as f:
    pickle.dump(create_list(), f)

with open('animals.pickle', 'rb') as f:
    lst = pickle.load(f)
for i in lst:
    print(f'{i.say_species()} {i.say_name()} говорит {i.make_sound()}')
