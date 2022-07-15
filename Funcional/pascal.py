def bordes1(l):
    return [1] + l + [1]

def elementop(e):
    return bordes1([i+j for i,j in zip(e[1:],e[:-1])])

def nivelp(l):
    return l + [elementop(l[-1])]

def pascal(n):
    if n == 1:
        return [[1]]
    else:
        return nivelp(pascal(n-1))

def triangulo(l):
    if l:
        [print(" ",end='') for i in range(len(l)*3//2)]
        [print("{:2d} ".format(i),end='') for i in l[0]]
        print()
        return triangulo(l[1:])

triangulo(pascal(8))