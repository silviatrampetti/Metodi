import numpy as np

def somma_n(n):
    num = np.arange(1,n+1)
    s = np.sum(num)
    return s
    
def somma_radici(n):
    num = np.arange(1,n+1)
    rad = np.sqrt(num)
    s = np.sum(rad)
    return s

