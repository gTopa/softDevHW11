def intersection(a,b):
    [val for val in a if val in b]

def union(a,b):
    [val for val in a.extend(b) if (val in a) and (val in b)]

def setDif(u,a):
    [val for val in u if !(val in a)]

def symDif(a,b):
    setDif(union(a,b),intersection(a,b))

def cartProd(a,b):
    l=[]
    for val in a:
        l.append([(val, i) for i in b])
