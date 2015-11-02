"""This module contains the unit tests of the hw7 program"""

import numpy as np 
from unittest import TestCase
import unittest
import create_2d_array
import divide_array
import mandelbrot
import math
#author: Muhe Xie
#netID: mx419
#date: 11/01/2015


class Test_HW7(TestCase):
    '''this class will test the functions and methods of classes in homework7'''
    def setUp(self):
        pass

    def test_array_2d_operations(self):
        '''the method will test answers for question 1'''
        #answer a 
        answer_1a = np.array([[2,7,12],[4,9,14]])
        #answer b
        answer_1b = np.array([6,7,8,9,10])
        #answer c 
        answer_1c = np.array([[ 2,  7, 12],[ 3,  8, 13],[ 4 , 9, 14]])

        instance_1 = create_2d_array.Array_2D_Operations()
        self.assertTrue(np.array_equal(answer_1a,instance_1.generate_array_2nd_4th_row()))
        self.assertTrue(np.array_equal(answer_1b,instance_1.generate_array_2nd_column()))
        self.assertTrue(np.array_equal(answer_1c,instance_1.generate_array_in_rec_section()))

    def test_divide_array(self):
        '''the method will test answers for question 2'''
        answer_2_pos_1_1 = 1.2
        answer_2_pos_4_0 = 1.
        instance_2 = divide_array.Divide_Array()
        self.assertEqual(answer_2_pos_4_0,instance_2.generate_divided_array()[4,0])
        self.assertEqual(answer_2_pos_1_1,instance_2.generate_divided_array()[1,1])

    def test_mandelbrot(self):
        '''the method will test answers for mandelbrot module'''
        self.assertTrue(mandelbrot.calculate_iteration(0+1j*1))
        self.assertFalse(mandelbrot.calculate_iteration(1+1j*1))
        mask = mandelbrot.generate_mask_array(3)
        self.assertFalse(mask[0,0])
        self.assertTrue(mask[0,1])


if __name__ == '__main__':
    unittest.main()


        

