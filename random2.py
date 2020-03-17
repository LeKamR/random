#usr/bin/env python
from datetime import *
from math import *
n=int(input("Generate a random integer between 0 and n. n=? ")) 
def random(n):
    x=datetime.now()
    x=str(x.microsecond)
    x=int(x)
    m=datetime.now()
    m=str(m.microsecond)
    m=int(m)
    x=x**3+256-m
    x+= 536
    x=x%n
    print(x)
random(n)

