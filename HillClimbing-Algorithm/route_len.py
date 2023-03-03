def routelen(route, distmat):
    """Calculates the length of a route"""
    route_len = 0
    for i in range(len(route)):
        route_len += distmat[route[i-1]][route[i]]
    return route_len