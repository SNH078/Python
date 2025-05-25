# operator can be overloaded using dunder method
# these methods are called when a given operator is unsed on the objects 
# p1+p2 # p1.__add__(p2) 
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)
# p1.__xor__(p2)
# p1.__pos__
"""
class number:
    def __init__(self,n):
        self.n=n

n=number(1)
m=number(2)

print(n+m) 
"""

class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n # Overloading the '+' operator

n=number(1)
m=number(2)
print(4+2)
print(n+m)  #  n.__add__(m)  => self.n++num.n