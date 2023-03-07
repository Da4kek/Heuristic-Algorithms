import numpy as np 
import copy 

def mutate(c,mu,sigma):
    y = copy.deepcopy(c)
    flag = np.random.rand(*c['position'].shape) <= mu 
    ind = np.argwhere(flag == True)
    y['position'][ind] += sigma*np.random.randn(*ind.shape) 
    return y 