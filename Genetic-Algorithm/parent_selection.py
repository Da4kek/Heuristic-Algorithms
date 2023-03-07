import numpy as np 

def roulette_wheel_selection(p):
    c = np.cumsum(p) 
    r = sum(p)*np.random.rand() 
    ind = np.argwhere(c>=r) 
    return ind[0][0]