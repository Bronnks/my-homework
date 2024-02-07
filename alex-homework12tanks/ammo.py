from abc import ABC
from abc import abstractmethod
from gun import Gun


__all__ = (
    'Ammo', 'AmmoRack', 'Blank',
    'APCartridge',
    'HECartridge',
    'HEATCartridge',
)
class AmmoRack(ABC):
    def __init__(self):
        self.rack = {'фугасный': [], 'кумулятивный': [], 'подкалиберный': []}

    def __load_ammo(self, name):
        self.rack[name.ammo_type].append(name)

    def load(self, name):
        self.__load_ammo(name)

    def removes(self, name: str):
        return self.rack[name].pop(-1)


class Ammo(AmmoRack):

    def __init__(self, gun: Gun, ammo_type: str):
        super().__init__()
        self.gun = gun
        self.ammo_type = ammo_type

    @abstractmethod
    def get_damage(self) -> float:
        return self.gun.get_caliber() * 3

    def get_penetration(self):
        return self.gun.get_caliber()

    def __str__(self):
        return f'Снаряд {self.ammo_type} к пушке калибра {self.gun.get_caliber()}'


class APCartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'подкалиберный')

    def get_damage(self) -> float:
        damage = super().get_damage() * 0.3
        print(f'Пробивший броню снаряд имеет тип {self.ammo_type}. Нанесенный урон = {damage}')
        return damage


class HECartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'фугасный')

    def get_damage(self) -> float:
        damage = super().get_damage() * 1.0
        print(f'Пробивший броню снаряд имеет тип {self.ammo_type}. Нанесенный урон = {damage}')
        return damage


class HEATCartridge(Ammo):

    def __init__(self, gun: Gun):
        super().__init__(gun, 'кумулятивный')

    def get_damage(self) -> float:
        damage = super().get_damage() * 0.6
        print(f'Пробивший броню снаряд имеет тип {self.ammo_type}. Нанесенный урон = {damage}')
        return damage
    
    
class Blank(Ammo):
    def __init__(self, gun: Gun):
        super().__init__(gun, 'холостой')

    def get_damage(self) -> float:
        return 0
