class A:
    A = 1
    def __init__a(self):
        self.a =0

#o=A(1)
print("'hasattr:", hasattr(A, 'a'))

import math
print (dir(math))

class Class:
    def __init__(self, val=0):
        pass

obj = Class(1)
obj1 = Class(None)

from datetime import timedelta
delta = timedelta(weeks=1, days=7, hours=11)
print("delta:",delta*2)

numbers = [i*i for i in range(5)]
foo = list(filter(lambda x:x%2, numbers))
print ("foo:", foo)

print(float("1.3"))

class A:
    def __init__ (self, v=2):
        self.v=v

    def set (self, v=1):
        self.v += v
        return self.v

a = A()
b = a
b.set()
print (a.v)