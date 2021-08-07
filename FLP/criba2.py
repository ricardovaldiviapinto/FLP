def criba (n):
    return list(range(2, n+1))

def eliminar(m, l):
    return list(filter(lambda x: x%m != 0, l))

from math import sqrt

def tamizar(n, l):
    if l[0] > sqrt(n):
        return l
    else:    
        return [l[0]] + tamizar(n, (eliminar (l[0], l)))

def eratostenes(n):
    return tamizar(n, criba(n))

print(eratostenes(100))