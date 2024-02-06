class Vehicle:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    @staticmethod
    def start():
        print("The vehicle is starting")

    def print_info(self):
        for i, v in self.__dict__.items():
            print(f'{i} - {v}', end='. ')


class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        super().__init__(brand, model, color)
        self.doors = doors

    @staticmethod
    def honk():
        print("The car is honking")


class Bike(Vehicle):
    def __init__(self, brand: str, model: str, color: str, gears: int):
        super().__init__(brand, model, color)
        self.gears = gears

    @staticmethod
    def pedal():
        print("The bike is pedaling")


class Plane(Vehicle):
    def __init__(self, brand: str, model: str, color: str, wingspan: int):
        super().__init__(brand, model, color)
        self.wingspan = wingspan

    @staticmethod
    def fly():
        print("The plane is flying")
