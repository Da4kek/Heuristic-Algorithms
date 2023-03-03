from create_nodes import NodeGen
from SimulatedAnnealing import SimulatedAnnealing

def tsp():
    temp = 1000
    stoping_time = 0.000001
    alpha = 0.999
    stoping_temp = 0.000001
    size_width = 200 
    size_height = 200

    population_size = 70

    nodes = NodeGen(size_width,size_height,population_size).gen_()
    sa = SimulatedAnnealing(nodes,temp,alpha,stoping_temp,stoping_time)
    sa.anneal()
    sa.plotlearning()

tsp()