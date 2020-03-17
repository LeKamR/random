#usr/bin/env python
from datetime import *
from math import *
def random():
    x=datetime.now()
    x=str(x.microsecond)
    x=int(x)
    n=datetime.now()
    n=str(n.microsecond)
    n=int(n)
    x=x**3+256-n
    x+= 536
    x=x%10
    print(x)
random()


