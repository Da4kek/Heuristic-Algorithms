import numpy as np 
from genetics import ga
import matplotlib.pyplot as plt 
costfunc = lambda x:sum(x**2)
num_var = 5 
varmin = -10 
varmax = 10  
maxit = 501 
npop=20 
beta = 1 
prop_children = 1 
num_children = int(np.round(prop_children*npop/2)*2)
mu = 0.2 
sigma = 0.1 
out = ga(costfunc,num_var,varmin,varmax,maxit,npop,num_children,mu,sigma,beta)

plt.plot(out[2])
plt.xlim(0,maxit)
plt.xlabel("Generations")
plt.ylabel("Cost") 
plt.title("Genetic algorithm") 
plt.grid(True) 
plt.show()