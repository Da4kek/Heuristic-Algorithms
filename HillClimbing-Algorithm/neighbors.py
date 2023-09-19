from route_len import routelen


def get_neighbors(solution):
    
    neighbors = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def get_best_neighbors(solution, distmat):
    
    best_neighbor = solution
    best_len = routelen(solution, distmat)
    for neighbor in get_neighbors(solution):
        neighbor_len = routelen(neighbor, distmat)
        if neighbor_len < best_len:
            best_neighbor = neighbor
            best_len = neighbor_len
    return best_neighbor
