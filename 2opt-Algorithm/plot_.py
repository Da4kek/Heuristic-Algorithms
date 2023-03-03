import matplotlib.pyplot as plt 
import numpy as np 
from tsp import two_opt,path_distance

cities = np.random.rand(70,2) 
route = two_opt(cities,0.001)

new_cities_order = np.concatenate((cities[route],cities[route[0]].reshape(1,2)))
print(f"Cities: {cities}")

plt.scatter(cities[:,0],cities[:,1])
plt.plot(new_cities_order[:,0],new_cities_order[:,1],'--',color='red')
plt.show()
print(f"Route distance: {path_distance(route,cities):.2f}")