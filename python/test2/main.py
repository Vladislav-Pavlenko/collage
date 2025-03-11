class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calcPerimeter(self):
        return 2*(self.length+self.width)

    def calcSquare(self):
        return self.width*self.length

obj = Rectangle(4, 5)

print(obj.calcPerimeter())
print(obj.calcSquare())