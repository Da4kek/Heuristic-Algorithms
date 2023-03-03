import random 
import numpy as np 

class NodeGen:
    def __init__(self,width,height,nodesNum):
        self.width = width
        self.height = height
        self.nodesNum = nodesNum
    
    def gen_(self):
        x = np.random.randint(self.width,size=self.nodesNum)
        y = np.random.randint(self.height,size=self.nodesNum)
        return np.column_stack((x,y))