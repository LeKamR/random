#usr/bin/env python
from datetime import *
from math import *
def random():
    x=datetime.now()
    x=x.microsecond
    x=map(int,str(x))
    x=sum(x)
    x=int(x**3+256+exp(x+3))
    x+= 536
    x=x%10
    print(x)
random()


