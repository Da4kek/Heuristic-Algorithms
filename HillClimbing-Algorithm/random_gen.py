import random
def random_solution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        city = cities[random.randint(0,len(cities)-1)]
        solution.append(city)
        cities.remove(city)
    return solution
