"""This module contain user_defined exceptions"""

#author: Muhe Xie
#netID: mx419
#date: 11/01/2015


class Plot_Matrix_Empty_Error(Exception):
    '''raised when plot matrix is empty'''
    def __str__(self):
        return 'plot matrix is empty' 
