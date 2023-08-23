def metade(n):
    n /= 2
    return n


def dobro(n):
    n *= 2
    return n


def aumento(n, porcent = 0):
    p = porcent / 100
    n *= (1 + p)
    return n

def reducao(n, porcent = 100):
    p = porcent / 100
    t = n * p
    n = n - t
    return n 
