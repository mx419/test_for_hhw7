"""This module contain a class to solve Question 3. The class contain the random 2-Darray and a method to generate an array with selected elements"""

import numpy as np 

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

class Select_Elements:
    """The class contain the 10*3 2-Darray in Question3 and a method to generate the array contains elements closest to 0.5"""
    def __init__(self):
        '''the constructor will generate the basic 10*3 array'''
        np.random.seed(10)
        self.array_10x3 = np.random.rand(10,3)

    def select_elements(self):
        '''the method will generate the result contains the elements closest to 0.5'''
        #generate an array  with values 0.5
        array_standard = np.repeat(0.5,30).reshape(10,3) 
        #compute the difference with 0.5
        array_diff = abs(self.array_10x3 - array_standard)
        #select the columns
        array_indexes = np.argsort(array_diff,axis=1)[:,0]
        final_result = self.array_10x3[np.arange(len(self.array_10x3)),array_indexes]
        return final_result





