import random
import numpy as np
from deap import base, creator, tools, algorithms

class GenP():
    def __init__(self, cities, pop_rate, gen):
        self.cities = cities
        self.pop_rate = pop_rate
        self.gen = gen

    def distance(self, city1, city2):
        return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def eval_tour(self, individual):
        tour = [str(x) for x in individual]

        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += self.distance(self.cities[tour[i]], self.cities[tour[i + 1]])
        total_distance += self.distance(self.cities[tour[-1]], self.cities[tour[0]])

        return total_distance,

    def simulate(self):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("indices", random.sample, range(len(self.cities)), len(self.cities))
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", self.eval_tour)
        toolbox.register("mate", tools.cxOrdered)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=self.pop_rate)

        for gen in range(self.gen):
            offspring = algorithms.varAnd(population, toolbox, cxpb=0.7, mutpb=0.2)
            fitnesses = list(map(toolbox.evaluate, offspring))
            for ind, fit in zip(offspring, fitnesses):
                ind.fitness.values = fit

            population[:] = offspring

        best_individual = tools.selBest(population, k=1)[0]
        best_tour = best_individual

        return best_tour, best_tour.fitness.values[0]

