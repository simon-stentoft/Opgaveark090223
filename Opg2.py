'''
Opret en klasse Punkt med medlems variable x, y og navn(char).
Implementer konstruktør, og metoderne:
set_navn, get_navn, set_x, get_x, set_y, get_y, flyt_x_retning, flyt_y_retning, flyt_xy_retning,
dist_til_punkt (afstanden til et andet punkt)

Implementer overloading af operatorerne: == og !=

Test klassen.

'''

class Punkt:
    def __init__(self, x, y, navn):
        self.x = x
        self.y = y
        self.navn = navn
    
    def set_navn(self, navn):
        self.navn = navn
    
    def get_navn(self):
        return self.navn
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def flyt_x_retning(self, x):
        self.x += x
    
    def flyt_y_retning(self, y):
        self.y += y
    
    def flyt_xy_retning(self, x, y):
        self.x += x
        self.y += y
    
    def dist_til_punkt(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    

a = Punkt(1, 2, "Abe")

print(a.get_navn())
a.set_navn("Banan")
print(a.get_navn())

a.set_x(3)
print(a.get_x())

a.set_y(4)
print(a.get_y())

a.flyt_x_retning(5)
print(a.get_x())

a.flyt_y_retning(6)
print(a.get_y())

a.flyt_xy_retning(7, 8)
print(a.get_x(), a.get_y())

print(a.dist_til_punkt(1, 2))

print(a == Punkt(1, 2, "Abe"))
print(a != Punkt(1, 2, "Abe"))

