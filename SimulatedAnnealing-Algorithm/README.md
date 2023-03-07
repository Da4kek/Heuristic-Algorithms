# Simulated Annealing Algorithm
---
> Simulated annealing is a probabilistic technique for approximating the global optimum of a given function. Simulated annealing is a metaheuristic to approximate global optimization in a large search space. It is often used when the search space is discrete *(e.g., all tours that visit a given set of cities).* It is frequently used when the search problem has many local minima, possibly of equal value (so called multimodal problems). It may be applied to continuous spaces, but is more useful in discrete optimization problems for which global optimization is difficult. Simulated annealing is related to the simulated tempering method, which is a special case of simulated annealing.

**Formula:**
`P = e^((f(x) - f(x'))/T)`
(or)
`Prob(accepting uphill move)~1-exp(deltaE/KT)`
where,
`P` is the probability of accepting an uphill move,
`f(x)` is the value of the objective function at the current state,
`f(x')` is the value of the objective function at the new state,
`T` is the temperature,
`K` is the Boltzmann constant,
`deltaE` is the change in energy between the current state and the new state.

---

## Simple example:
```python
def simulated_annealing(f, x0, T, alpha, max_iter):
    x = x0 # current best solution
    for i in range(max_iter):
        T = alpha * T # decrease temperature
        if T < 1e-8: # stop if temperature is very low
            return x
        neighbors = get_neighbors(x) # get neighbors of current solution
        x' = random.choice(neighbors) # choose a random neighbor
        if f(x') < f(x): # if neighbor is better, move to it
            x = x'
        else: # if neighbor is worse, move to it with a probability of P
            P = e^((f(x) - f(x'))/T)
            if random.random() < P:
                x = x'
```
![Simulated Annealing](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*iXV2btukAUcn5lfd-ZjU7A.png)