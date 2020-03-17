#usr/bin/env python
from datetime import *
from math import *
n=int(input("Generate a random integer between 0 and n"))
def random(n):
    x=datetime.now()
    x=x.microsecond
    x=map(int,str(x))
    x=sum(x)
    x=int(x**3+256+exp(x+3))
    x+= 536
    x=x%n
    print(x)
for i in range (0,10):
    random(n)

