"""This module contain two functions to solve Question 4. Two functions will form a 2-D boolean mask indicating which points are in the set"""

import numpy as np 
import math
import matplotlib.pyplot as plt


#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

def calculate_iteration(c):
    '''the function will calculate the iteration result of a specific complex number
    args: c is the  complex number 
    return: boolean value indicate whether the point is in the set
    '''
    N_max = 50 #iteration time
    some_threshold = 50 #threshold to judge whether it is in the set
    z = c
    for v in range(N_max):
        z = z**2 + c
        if abs(z) >= some_threshold:
            return False
    return True

def generate_mask_array(N):
    '''the function will generate a mask with value True and False
    args: N is the size of the N*N mask matrix
    return: mask matrix with boolean values
    '''
    x_array = np.linspace(-2.,1.,num=N)
    y_array = np.linspace(-1.5,1.5,num=N)
    complex_grid = np.array(range(N*N), dtype=complex).reshape(N,N) 
    mask_array = np.array(np.arange(N*N), dtype=bool).reshape(N,N)
    for i in range(N):
        for k in range(N):
            complex_grid[i][k] = x_array[i]+1j*y_array[k]
            mask_array[i][k] = calculate_iteration(complex_grid[i][k])

    return mask_array
