def listadiv(n, m):
    if n == 1:
        return [[n, m]]
    else:
        return [[n,m]] + listadiv(n//2,m*2)

def listamult(l):
    return [j for i,j in l if i%2 != 0]

def rusa(n, m):
    return sum(listamult(listadiv(n, m)))