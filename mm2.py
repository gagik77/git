import turtle

def draw_figure(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def main():
    turtle = turtle.Turtle()
    draw_figure(turtle)
    turtle.done()

if __name__ == '__main__':
    main()



class Figure:
    def __init__(self):
        self.name = 'Figure'

    def area(self):
        raise NotImplementedError

    def __int__(self):
        return self.area()

    def __str__(self):
        return f'{self.name}: area = {self.area()}'

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.name = 'Rectangle'

    def area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = 'Circle'

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class Trapeze(Figure):
    def __init__(self, a, b, h):
        super().__init__()
        self.a = a
        self.b = b
        self.h = h
        self.name = 'Trapeze'

    def area(self):
        return (self.a + self.b) * self.h / 2
    


