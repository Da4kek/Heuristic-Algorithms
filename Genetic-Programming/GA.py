import numpy as np 
import random

class GenA():
    def __init__(self,cities,pop_size,gen,mr) -> None:
        self.cities = cities 
        self.pop_size = pop_size
        self.gen = gen 
        self.mr = mr 
    
    def distance(self,x,y):
        x1,y1 = self.cities[x]
        x2,y2 = self.cities[y]
        return np.sqrt((x1-x2) **2 + (y1-y2) **2)
    
    def create_pop(self):
        population = [list(self.cities.keys()) for _ in range(self.pop_size)]
        for i in range(self.pop_size):
            random.shuffle(population[i])
        return population 

    def tour_distance(self,tour):
        return sum([self.distance(tour[i],tour[i+1]) for i in range(len(tour)-1)]) + self.distance(tour[-1],tour[0])
    
    def crossover(self,parent1,parent2):
        crossover_point = random.randint(0,len(parent1)-1)
        child = parent1[:crossover_point]
        for gene in parent2:
            if gene not in child:
                child.append(gene)
        return child
    
    def mutate(self,tour):
        if random.random() < self.mr:
            i,j = random.sample(range(len(tour)),2)
            tour[i],tour[j] = tour[j],tour[i]
        return tour 

    def simulate(self):
        population = self.create_pop()
        for _ in range(self.gen):
            population = sorted(population, key=lambda x: self.tour_distance(x))
            new_population = []
            new_population.append(population[0])
            while len(new_population) < self.pop_size:
                parent1,parent2 = random.sample(population,2)
                child = self.crossover(parent1,parent2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population
        best_tour = min(population,key = lambda x: self.tour_distance(x))
        return best_tour,self.tour_distance(best_tour)
