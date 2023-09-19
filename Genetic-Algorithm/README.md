# Genetic-Algorithm
---
> Genetic algorithms are a search heuristic that is inspired by the process of natural selection. This technique belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover, and selection.

**Types of Genetic Algorithms:**
* **Generational GA**: if the population size is P, there are P offspring that are created and mutated. The replacement strategy replaces all the parents with their offspring. This results in no overlap between the current and new population.
* **Steady-state GA**: works by randomly selecting two parents, creating one offspring, and replacing the worst fit individual in the population with the offspring. It makes only one function evaluation per child on each cycle.
* **Mu + GA**: works by randomly selecting two parents with binary tournament selection, creating an offspring and adding the offspring to a child population until the child population size is equal to the original population size.
---
## Terms:
* **Population:** A population is a set of solutions.
* **Individual:** An individual is a solution in the population.
* **Chromosome:** A chromosome is a set of genes.
* **Gene:** A gene is a value in the chromosome.
* **Fitness:** Fitness is a value that represents how good a solution is.
* **Selection:** Selection is the process of choosing individuals from the population.
---
## Simple example:
```python
import random
population_size = 100
genes = [0, 1]
target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
population = []
for i in range(population_size):
    population.append([random.choice(genes) for i in range(len(target))])
def fitness(individual): # Fitness function
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
            fitness += 1
    return fitness
def selection(population): # Selection function
    fitnesses = [fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    return random.choices(population, probabilities)[0]
def crossover(individual1, individual2): # Crossover function
    index = random.randint(0, len(individual1) - 1)
    return individual1[:index] + individual2[index:]
def mutation(individual): # Mutation function
    index = random.randint(0, len(individual) - 1)
    individual[index] = 1 if individual[index] == 0 else 0
    return individual
```
*Generational Genetic Algorithm:*
```python
def genetic_algorithm(population, fitness, selection, crossover, mutation, generations): 
    # Genetic algorithm
    for i in range(generations):
        new_population = []
        for j in range(len(population)):
            individual1 = selection(population)
            individual2 = selection(population)
            individual = crossover(individual1, individual2)
            individual = mutation(individual)
            new_population.append(individual)
        population = new_population
    return population
```
