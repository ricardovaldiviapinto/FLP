import pascal as psc

print(psc.triangulo(psc.pascal(8)))

# PROPIEDADES DEL TRIANGULO DE PASCAL
# https://www.youtube.com/watch?v=KX0vfHwfxu0&t=134s

# potencias en base dos, suma de cada fila del triángulo de pascal
def potencias2(l):
    return [sum(i) for i in l]

# numero naturales, segunda diagonal del triángulo de pasal
def naturales(l):
    return [l[1:][i][i] for i in range(0,len(l)-1)]

# numeros triangulares, tercera diagonal del triángulo de pascal
def triangulares(l):
    return [l[2:][i][i] for i in range(0,len(l)-2)]

# numeros cuadrados, suma de pares de componentes consecutivos de la diagonal de números triangulares
def cuadrados(l):
    t = triangulares(l)
    return [1] + [i+j for i,j in zip(t[:-1],t[1:])]

# numeros pentagonales, suma de (1,2,3,...) componentes consecutivos de la diagonal de número naturales
from math import ceil

def pentagonales(l):
    n = naturales(l)
    return [sum(n[i-1:i+n[i]-2]) for i in n[:ceil((n[-1]/2))]]

# numeros hexagonales, componentes impares de la diagonal de números triangulares
def hexagonales(l):
    return [l[2:][i][i] for i in range(0,len(l)-2,2)]

# triangulo de sierpinski
def triangulo_spky(l):
    if l:
        [print(" ",end='') for i in range(len(l)*3//2)]
        [print((lambda x: '*' if x%2 else ' ')(i),end='  ') for i in l[0]]
        print()
        return triangulo_spky(l[1:])

print(triangulo_spky(psc.pascal(8)))
