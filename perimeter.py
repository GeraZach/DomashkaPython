class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def per(self):
        return self.a+self.b+self.c


PerimeterTreugolnika = Triangle(15, 20, 25)
print('Perimeter of a triangle: ')
print(PerimeterTreugolnika.per())


class Square:
    def __init__(self,a):
        self.a = a

    def per(self):
        return self.a*4


PerKvadrat = Square(20)
print('Perimeter of a square: ')
print(PerKvadrat.per())


class Parallelogram:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def per(self):
        return self.a+self.b+self.c+self.d


PerParall = Parallelogram(20, 10, 30, 40)
print('Parall per equals: ')
print(PerParall.per())