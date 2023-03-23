'''Færdiggør klassen Broek, med overloading af operatorerne:
==, !=, <=, <, >= og >

Test klassen.'''


class Broek:
    def __init__(self, t, n):
        self.t = t
        self.n = n
    
    def __eq__(self, other):
        return self.t * other.n == self.n * other.t
    
    def __ne__(self, other):
        return self.t * other.n != self.n * other.t
    
    def __le__(self, other):
        return self.t * other.n <= self.n * other.t
    
    def __lt__(self, other):
        return self.t * other.n < self.n * other.t
    
    def __ge__(self, other):
        return self.t * other.n >= self.n * other.t
    
    def __gt__(self, other):
        return self.t * other.n > self.n * other.t
    

a = Broek(3, 4)
b = Broek(6, 9)

print("==", a == b)
print("!=", a != b)
print("<=", a <= b)
print("<", a < b)
print(">=", a >= b)
print(">", a > b)





    
