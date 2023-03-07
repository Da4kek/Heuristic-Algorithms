# 2-opt Algorithm:
---
> In optimization, 2-opt is a simple local search algorithm for solving the traveling salesman problem. The main idea behind it is to take a route that crosses over itself and find a way to remove the crossing over. This is done by swapping two edges that are connected to the same two vertices. This algorithm is a heuristic, meaning that it does not always find the optimal solution, but it is fast and simple to implement. The algorithm is named after the fact that it involves swapping two edges, hence the name 2-opt.

**Formula:**
`Length of the new route = Length of the old route - (Length of the edge that is being removed) + (Length of the new edge that is being added)`
(or)
`Length Delta = -dist(route[v1],route[v2]) - dist(route[v3],route[v4]) + dist(route[v1],route[v3]) + dist(route[v2],route[v4])`
where,
`v1 = route[i-1]`
`v2 = route[i]`
`v3 = route[k-1]`
`v4 = route[k]`

---

## Procedure:
1. Take route[0] to route[v1] and add them in order to new_route.
2. Take route[v1] to route[v2] and add them in reverse order to new_route.
3. Take route[v2] to route[v3] and add them in order to new_route.


**Visualization:**
![visualization](https://upload.wikimedia.org/wikipedia/commons/f/f6/2-opt_Swap_Path_Visualization.gif)
(*Source*: [Wikipedia](https://en.wikipedia.org/wiki/2-opt))

---

## Simple example:
Let's say we have a route that looks like this:
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]`
and we want to swap the edges between 2 and 5 and 3 and 4. The new route would look like this:
`[0, 1, 5, 4, 3, 2, 6, 7, 8, 9, 0]`

```python
def 2-opt(route):
    new_route = []
    for i in range(0, v1):
        new_route.append(route[i])
    for i in range(v1, v2):
        new_route.append(route[v2 - i + v1])
    for i in range(v2, len(route)):
        new_route.append(route[i])
    return new_route
```