#usr/bin/env python
from datetime import *
n=int(input("Generate a random natural integer inferior to n. n=? ")) 
def randmax(n):
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
randmax(n)

