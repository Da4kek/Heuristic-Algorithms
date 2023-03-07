import numpy as np 
import copy 

def bounds(c,varmin,varmax):
    c['position'] = np.maximum(c['position'],varmin)
    c['position'] = np.minimum(c['position'],varmax)

def sort(arr):
    n = len(arr)  
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]['cost'] > arr[j+1]['cost']:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
        return arr