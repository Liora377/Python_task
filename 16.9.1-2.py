class Rectangle:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.a}, {self.b}'

    def get_area(self):
        return self.a * self.b

rec = Rectangle(5, 10, 50, 100)

print(rec)
print(rec.get_area())