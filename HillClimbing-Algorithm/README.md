# Hill Climbing Algorithm:
---
> Hill climbing is a local search algorithm that is used to find a local optimum. A local optimum is a solution that is better than all other solutions in the neighborhood of the solution. A neighborhood is a set of solutions that are close to the solution. Hill climbing algorithms are used to find a local optimum by moving from one solution to another solution in the neighborhood. The algorithm stops when it reaches a local optimum.
---
**Types of Hill Climbing:**
* **Steepest Ascent Hill Climbing:** In this algorithm, the algorithm moves to the neighbor that has the highest value. This algorithm is also known as the greedy algorithm.
* **Simple Hill Climbing:** In this algorithm, the algorithm moves to a random neighbor. This algorithm is also known as the random restart algorithm.
* **Stochastic Hill Climbing:** In this algorithm, the algorithm moves to a random neighbor with a probability of moving to a worse neighbor. This algorithm is also known as the random walk algorithm.
  

![Hill Climbing](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210726172958/objectfuntion.png)

---
### Simple example:
```python
def hill_climbing(f,x0):
    x = x0 # current best solution
    while True:
        neighbors = get_neighbors(x) # get neighbors of current solution
        if not neighbors:
            return x # local optimum
        x = min(neighbors, key=f) # move to the neighbor with the lowest value
    