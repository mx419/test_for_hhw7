"""
This module contain a class to solve Question 1. The class contain the 2-D array and corresponding methods.
The class's methods will generate answers for question a to d
"""

import numpy as np 

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015

class Array_2D_Operations:
    ''' This class contains the 2D numpy array in the question and methods to generate new arrays based on the 2D array'''
    def __init__(self):
        '''the constructor will generate the basic 2D array'''
        self.array_2D = np.arange(1,16,1).reshape(3,5).T

    def generate_array_2nd_4th_row(self):
        '''the method will generate an array contain 2nd and 4th rows in the basic 2D array'''
        array_row2_row4= self.array_2D[[1,3],:]
        return array_row2_row4

    def generate_array_2nd_column(self):
        '''the method will generate an array contain 2nd column in the basic 2D array'''
        array_2nd_column = self.array_2D[:,1:2]
        return array_2nd_column

    def generate_array_in_rec_section(self):
        '''the method will generate an array in the rectangular section between the coordinates [1,0] and [3,2]'''
        array_rec = self.array_2D[1:4,0:3]
        return array_rec

    def generate_array_3_to_11(self):
        '''the method will generate an array contains elements between 3 and 11'''
        array_d = self.array_2D.ravel()
        array_d.sort()
        array_d = array_d[np.logical_and((array_d>=3), (array_d<=11))]
        array_d_2D = array_d.reshape(1,len(array_d))
        return array_d_2D

