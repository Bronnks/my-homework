class Kilo:
    def __init__(self, value):
        if value < 0 or value >= 1000:
            raise ValueError
        self.value = value
        self.lb = round(self.value * 2.2046, 2)

    def __repr__(self):
        return f'Value = {self.value}, кг, = {self.value * 1000} грамм.'

    def convert_kilo_to_lb(self):
        print(f'{self.value} кг = {self.lb} lbs')

    def raise_value(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return self.value + n
        else:
            raise ValueError

    def __add__(self, other):
        if isinstance(self, Kilo) and isinstance(other, Kilo):
            return self.value + other.value
        elif isinstance(self, Kilo) and isinstance(other, Lb):
            return self.value + other.kilo
        elif isinstance(self, Kilo) and (isinstance(other, int) or isinstance(other, float)):
            return self.value + other
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(self, Kilo) and isinstance(other, Kilo):
            return self.value + other.value
        elif isinstance(self, Kilo) and isinstance(other, Lb):
            return self.value + other.kilo
        elif isinstance(self, Kilo) and (isinstance(other, int) or isinstance(other, float)):
            return self.value + other
        else:
            raise ValueError


class Lb:
    def __init__(self, value):
        if value < 0 or value >= 14:
            raise ValueError
        self.value = value
        self.kilo = round(self.value * 0.454, 2)

    def __repr__(self):
        return f'Value = {self.value}, фунт, = {self.value * 16} унций.'

    def convert_lb_to_kilo(self):
        print(f'{self.value} lbs = {self.kilo} кг')

    def raise_value(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return self.value + n
        else:
            raise ValueError

    def __add__(self, other):
        if isinstance(self, Lb) and isinstance(other, Lb):
            return self.value + other.value
        elif isinstance(self, Lb) and isinstance(other, Kilo):
            return self.value + other.lb
        elif isinstance(self, Lb) and (isinstance(other, int) or isinstance(other, float)):
            return self.value + other
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(self, Lb) and isinstance(other, Lb):
            return self.value - other.value
        elif isinstance(self, Lb) and isinstance(other, Kilo):
            return self.value - other.lb
        elif isinstance(self, Lb) and (isinstance(other, int) or isinstance(other, float)):
            return self.value - other
        else:
            raise ValueError

