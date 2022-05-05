from rectangle import Rectangle, Square, Circle

# создадим 2 прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# квадраты

square_1 = Square(5)
square_2 = Square(10)

# круги

circle_1 = Circle(5)
circle_2 = Circle(23)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())