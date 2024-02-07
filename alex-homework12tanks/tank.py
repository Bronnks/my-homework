import random

from gun import Gun
from ammo import *
from armour import *
from ammo import Ammo, AmmoRack, Blank


class CrewMate:
    def __init__(self, name: str, lastname: str, rank: str, specialty: str):
        self.name = name
        self.lastname = lastname
        self.rank = rank
        self.specialty = specialty

        self.contusion = False
        self.condition = 'в порядке'

    def get_contusion(self, shoot: bool):
        self.contusion = shoot
        if self.contusion:
            self.condition = 'контужен'


class Commander(CrewMate):
    pass


class Gunner(CrewMate):
    pass


class Crew:
    def __init__(self, c: Commander, g: Gunner):
        self.list = [c, g]
        self.comm_status_ok = True
        self.gunner_status_not_ok = False

    def check_contusion(self):
        for i in self.list:
            i.get_contusion(random.choice((True, False)))

    def im_ok(self):
        for i in self.list:
            i.condition = 'в порядке'

    def condition_status(self):
        for i in self.list:
            if isinstance(i, Commander) and i.condition == 'контужен':
                self.comm_status_ok = False
            elif isinstance(i, Gunner) and i.condition == 'контужен':
                self.gunner_status_not_ok = True


class Panzer:
    def __init__(self, model: str, gun: Gun, armour_thickness: int, health: int, crew: Crew):
        self.model = model
        self.gun = gun
        self.armour_thickness = armour_thickness
        self.health = health

        self.ammos = AmmoRack()
        self.armours = []

        self.__load_ammos()
        self.__add_armours()

        self.selected_armour = self.armours[0]
        self.loaded_ammo = None
        self.crew = crew

    def __str__(self):
        return (f'Танк {self.model}; Здоровье = {self.health}; Заряженный снаряд: {self.loaded_ammo};'
                f' Выбранная броня: {self.selected_armour.armour_type}; Состояние экипажа: {self.crew.list[0].rank} '
                f'{self.crew.list[0].lastname} - {self.crew.list[0].condition}, '
                f'{self.crew.list[1].rank} {self.crew.list[1].lastname} - {self.crew.list[1].condition}')

    def __load_ammos(self):
        for i in range(5):
            self.ammos.load(APCartridge(self.gun))
            self.ammos.load(HEATCartridge(self.gun))
            self.ammos.load(HECartridge(self.gun))

    def __add_armours(self):
        self.armours.append(SArmour(thickness=self.armour_thickness))
        self.armours.append(HArmour(thickness=self.armour_thickness))
        self.armours.append(CArmour(thickness=self.armour_thickness))

    def load_gun(self, ammo_type: str):
        for ammo in self.ammos.rack:
            if ammo == ammo_type:
                if len(self.ammos.rack[ammo]) == 0:
                    self.loaded_ammo = Blank(self.gun)
                    print(f'{ammo_type.replace('й', 'e')} cнаряды закончились.')
                    return
                else:
                    self.loaded_ammo = self.ammos.removes(ammo)
                    print(f'Заряжено! Снаряд {ammo_type}.')
                    return

    def select_armour(self, armour_type: str):
        for armour in self.armours:
            if armour.armour_type == armour_type:
                self.selected_armour = armour
                break

    def shoot(self):
        if self.loaded_ammo is None:
            print('не заряжено')
            return
        elif isinstance(self.loaded_ammo, Blank):
            print('Закончились снаряды данного типа. Игрок пропускает ход.')
            return
        fired_ammo = self.loaded_ammo
        print(f'Танк {self.model} выстрелил {self.loaded_ammo} снаряд......')

        self.loaded_ammo = None

        dice = random.randint(0, 100)
        if self.crew.gunner_status_not_ok:
            dice //= 2
            self.crew.list[1].condition = 'в порядке'
        print(dice)
        if self.gun.is_on_target(dice):
            print('Попадание!')
            return fired_ammo
        else:
            print('Промах!')
            return None

    def handle_hit(self, projectile: Ammo):
        if self.selected_armour.is_penetrated(projectile):
            self.crew.check_contusion()

            self.health -= projectile.get_damage()
        else:
            print('Броня не пробита.')

    def get_health(self):
        return self.health
