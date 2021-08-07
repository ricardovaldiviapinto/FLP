def limites(n):
    return [(n*(n-1)//2) + 1, n*(n+1)//2]

def nivel(l):
    return [i for i in range(l[0],l[1]+1)]

def floyd(n):
    return [nivel(limites(i)) for i in range(1,n+1)]

def triangulo(l):
    if l:
        [print("{:2d} ".format(i),end='') for i in l[0]]
        print()
        return triangulo(l[1:])

triangulo(floyd(10))