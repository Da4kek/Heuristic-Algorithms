import numpy as np
import copy
from parent_selection import roulette_wheel_selection
from crossover import crossover
from utils import bounds, sort
from Mutate import mutate


def ga(costfunc, num_var, varmin, varmax, maxit, npop, num_children, mu, sigma, beta):

    population = {}
    for i in range(npop):
        population[i] = {'position': None, 'cost': None}

    bestsol = copy.deepcopy(population)
    bestsol_cost = np.inf

    for i in range(npop):
        population[i]['position'] = np.random.uniform(varmin, varmax, num_var)
        population[i]['cost'] = costfunc(population[i]['position'])

        if population[i]['cost'] < bestsol_cost:
            bestsol = copy.deepcopy(population[i])

    bestcost = np.empty(maxit)

    for it in range(maxit):

        costs = []
        for i in range(len(population)):
            costs.append(population[i]['cost'])
        costs = np.array(costs)
        avg_cost = np.mean(costs)
        if avg_cost != 0:
            costs = costs/avg_cost
        probs = np.exp(-beta*costs)

        for _ in range(num_children//2):

            p1 = population[roulette_wheel_selection(probs)]
            p2 = population[roulette_wheel_selection(probs)]

            c1, c2 = crossover(p1, p2)

            c1 = mutate(c1, mu, sigma)
            c2 = mutate(c2, mu, sigma)

            bounds(c1, varmin, varmax)
            bounds(c2, varmin, varmax)

            c1['cost'] = costfunc(c1['position'])

            if type(bestsol_cost) == float:

                if c1['cost'] < bestsol_cost:
                    bestsol_cost = copy.deepcopy(c1)
            else:

                if c1['cost'] < bestsol_cost['cost']:
                    bestsol_cost = copy.deepcopy(c1)

            if c2['cost'] < bestsol_cost['cost']:
                bestsol_cost = copy.deepcopy(c2)

        population[len(population)] = c1
        population[len(population)] = c2

        population = sort(population)

        bestcost[it] = bestsol_cost['cost']

        print('Iteration {}: Best Cost = {}'. format(it, bestcost[it]))

    out = population
    Bestsol = bestsol
    bestcost = bestcost
    return (out, Bestsol, bestcost)
