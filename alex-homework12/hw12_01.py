class Shape:
    def __init__(self, side: int):
        self.side = side

    def area(self):
        areas = self.side * 2
        print(f'Площадь фигуры = {areas}')

    def perimeter(self):
        perim = 4 * self.side
        print(f'Периметр фигуры = {perim}')


class Circle(Shape):
    def area(self):
        areas = self.side ** 2 * 3.14
        print(f'Площадь круга = {areas}')

    def perimeter(self):
        perim = 2 * self.side * 3.14
        print(f'Периметр круга = {perim}')


class Rectangle(Shape):
    def __init__(self, side: int, side2: int):
        super().__init__(side)
        self.side2 = side2

    def area(self):
        areas = self.side * self.side2
        print(f'Площадь квадрата = {areas}')

    def perimeter(self):
        perim = 2 * (self.side + self.side2)
        print(f'Периметр квадрата = {perim}')


class Triangle(Shape):
    def __init__(self, side: int, side2: int, side3: int):
        super().__init__(side)
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side + self.side2 + self.side3) / 2
        areas = (s * (s - self.side) * (s - self.side2) * (s - self.side3)) ** 0.5
        print(f'Площадь треугольника = {areas:.2f}')

    def perimeter(self):
        perim = self.side + self.side2 + self.side3
        print(f'Периметр треугольника = {perim}')
