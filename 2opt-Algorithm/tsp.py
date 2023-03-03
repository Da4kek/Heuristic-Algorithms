import numpy as np 

path_distance = lambda r,c:np.sum([np.linalg.norm(c[r[p]]-c[r[p-1]]) for p in range(1,len(r))])
two_opt_swap = lambda r,i,k:np.concatenate((r[0:i],r[k:-len(r)+i-1:-1],r[k+1:len(r)]))

def two_opt(cities,improvement_thres):
    route = np.arange(cities.shape[0])
    improvement_factor = 1
    best_distance = path_distance(route,cities)
    while improvement_factor > improvement_thres:
        distance_to_beat = best_distance
        for swap_first in range(1,len(route)-2):
            for swap_last in range(swap_first+1,len(route)):
                new_route = two_opt_swap(route,swap_first,swap_last)
                new_distance = path_distance(new_route,cities)
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
        improvement_factor = 1 - best_distance/distance_to_beat
    return route 
