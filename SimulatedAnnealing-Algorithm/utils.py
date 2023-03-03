import math
import numpy as np
import random 

def vec_to_distmatrix(coords):
    """Converts a vector of coordinates to a distance matrix."""
    dist = np.square(coords[:, np.newaxis] - coords)
    dist_sum = dist.sum(axis=2)
    return np.sqrt((dist_sum))

def nearestneighbour(dist_matrix):
    """Nearest neighbour algorithm for TSP."""
    node = random.randrange(len(dist_matrix))
    path = [node] 
    node_to_visit = list(range(len(dist_matrix)))
    node_to_visit.remove(node)

    while node_to_visit:
        nearest_node = min(node_to_visit, key=lambda x: dist_matrix[node][x])
        node_to_visit.remove(nearest_node)
        path.append(nearest_node)
        node = nearest_node
    return path