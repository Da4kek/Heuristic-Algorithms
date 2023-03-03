import math 
import random 
import matplotlib.pyplot as plt 
import utils 

class SimulatedAnnealing:
    def __init__(self,coords,temp,alpha,stop_temp,stop_iter):
        self.coords = coords
        self.sample_size = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stop_temp = stop_temp
        self.stop_iter = stop_iter
        self.iteration = 1

        self.dist_matrix = utils.vec_to_distmatrix(coords)
        self.curr_solution = utils.nearestneighbour(self.dist_matrix)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

        print('Intial weight: ', self.curr_weight) 
    
    def weight(self,sol):
        return sum([self.dist_matrix[i,j] for i,j in zip(sol,sol[1:]+[sol[0]])])
    
    def accept_prob(self,candidate_weight):
        return math.exp(-(candidate_weight - self.curr_weight)/self.temp)
    
    def accept(self,candidate):
        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate 
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate
        else:
            if random.random() < self.accept_prob(candidate_weight):
                self.curr_weight = candidate_weight
                self.curr_solution = candidate
    
    def anneal(self):
        """Anneal the solution."""
        while self.temp >=self.stop_temp and self.iteration < self.stop_iter:
            candidate = list(self.curr_solution)
            l = random.randint(2,self.sample_size-1)
            i = random.randint(0,self.sample_size-l)
            candidate[i:(i+l)] = reversed(candidate[i:(i+l)])
            self.accept(candidate)
            self.temp *= self.alpha
            self.iteration += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)
            print("Min weight: ", self.min_weight)
            print("Improvement: ", (self.initial_weight - self.min_weight)/self.initial_weight * 100, "%")
            print("Temperature: ", self.temp)

    def plotlearning(self):
        plt.plot([i for i in range(len(self.weight_list))],self.weight_list)
        line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        plt.legend((line_init,line_min),('Initial weight','Final weight'))
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.show()
        