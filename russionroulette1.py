from numpy import random

a=[1, 2, 3, 4, 5, 6]

def checknum(n):
    for x in a:
        if n==x:
            return(True)
    else:
          return(False)

n=int(input("open "))
c=checknum(n)


if c==False:
    print("redo")
    quit()
else:
    pass

k=random.randint(6)

if n==k:
    print("you fucking die")
else:
    print("got lucky bitch")