def routelen(route, distmat):
    route_len = 0
    for i in range(len(route)):
        route_len += distmat[route[i-1]][route[i]]
    return route_len
