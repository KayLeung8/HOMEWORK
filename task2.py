import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self):
        """Method documentation"""
        return


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Triangle: Consider me implemented", perim)
        return perim


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = (self.a + self.b) * 2
        print("Rectangle perimeter is:", perim)
        return perim


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)


rect = Rectangle(4, 5)
rect.calc_perimeter()

square = Square(4)
square.calc_perimeter()
