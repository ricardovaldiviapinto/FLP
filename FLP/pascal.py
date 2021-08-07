def bordesp(l):
    return [1] + l + [1]

def sumap(l):
    return [i+j for i,j in zip(l[:-1],l[1:])]

def nivelp(l):
    return bordesp(sumap(l[-1]))

def pascal(n):
    if n == 1:
        return [[1]]
    else:
        pas = pascal(n-1)       # me permito una impureza por razones de eficiencia 
        return pas + [nivelp(pas)]

def triangulo(l):
    if l:
        [print(" ",end='') for i in range(len(l)*3//2)]
        [print("{:2d} ".format(i),end='') for i in l[0]]
        print()
        return triangulo(l[1:])

triangulo(pascal(8))