from datetime import *
print("Generate a random natural integer between n and m (exclued)")
m=int(input("m= ?"))
n=int(input("n= ?"))
def randrange(mini=0,maxi=10):
    x=datetime.now()
    x=str(x.microsecond)
    x=int(x)
    y=datetime.now()
    y=str(y.microsecond)
    y=int(y)
    x=x**3+256-y
    x+= 536
    x=x%n
    if x<m:
        x+=y
        x=x%n
    print(x)
randrange(m,n)

