"""This module contain a class to solve Question 2. The class contain the 5*5 2-Darray and a method to generate the divided result"""

import numpy as np 

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

class Divide_Array:
    """The class contain the 5*5 2-Darray in Question2 and a method to generate the divided result"""
    def __init__(self):
        '''the constructor will generate the basic 5*5 array'''
        self.array_5_5 = np.arange(25,dtype=float).reshape(5, 5)

    def generate_divided_array(self):
        '''the method will generate the result of division'''
        divider = np.array([1., 5, 10, 15, 20])
        divide_result = self.array_5_5.T/divider
        divide_result = divide_result.T
        return divide_result

