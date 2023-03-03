from random_gen import random_solution
from route_len import routelen
from neighbors import get_neighbors,get_best_neighbors
import numpy as np

def hillclimbing(tsp):
    current_solution = random_solution(tsp)
    current_route_len = routelen(current_solution, tsp)
    neighbors = get_neighbors(current_solution)
    best_neighbor = get_best_neighbors(current_solution, tsp)
    best_neighbor_len = routelen(best_neighbor, tsp)

    while best_neighbor_len < current_route_len:
        current_solution = best_neighbor
        current_route_len = best_neighbor_len
        best_neighbor = get_best_neighbors(current_solution, tsp)
        best_neighbor_len = routelen(best_neighbor, tsp)
    return current_solution, current_route_len

tsp = np.random.randint(1,500,size = (4,4))
print(tsp)
print(hillclimbing(tsp))