import math


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Figure):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class RightTriangle(Figure):
    def __init__(self, x, y, leg1, leg2):
        super().__init__(x, y)
        self.leg1 = leg1
        self.leg2 = leg2

    def area(self):
        return 0.5 * self.leg1 * self.leg2

    def perimeter(self):
        hypotenuse = math.sqrt(self.leg1 ** 2 + self.leg2 ** 2)
        return self.leg1 + self.leg2 + hypotenuse


rect = Rectangle(0, 0, 5, 3)
circle = Circle(0, 0, 4)
triangle = RightTriangle(0, 0, 3, 4)

print(rect.area(), rect.perimeter())
print(circle.area(), circle.circumference())
print(triangle.area(), triangle.perimeter())