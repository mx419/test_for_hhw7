"""
This module is the main program. It generates the answers of homework7. Four modules
are writte to solve each question and will be called in this main program

"""
import numpy as np 
import math
import matplotlib.pyplot as plt
import create_2d_array
import divide_array
import mandelbrot
import select_array_elements

def generate_answe():
    '''the function will generate answers from 1 - 4'''
    #Question 1
    array_2D_answer = create_2d_array.Array_2D_Operations()
    #1.a generate an array contain 2nd and 4th rows in the basic 2D array
    print "Question 1a:"
    ans_Q1a = array_2D_answer.generate_array_2nd_4th_row()
    print ans_Q1a
    #1.b generate an array contain 2nd column
    print "Question 1b:"
    ans_Q1b = array_2D_answer.generate_array_2nd_column()
    print ans_Q1b
    #1.c generate an array in the rectangular section between the coordinates [1,0] and [3,2]
    print "Question 1c:"
    ans_Q1c = array_2D_answer.generate_array_in_rec_section()
    print ans_Q1c
    #1.d generate an array contains elements between 3 and 11
    print "Question 1d:"
    ans_Q1d = array_2D_answer.generate_array_3_to_11()
    print ans_Q1d

    #Question 2
    divide_array_answer = divide_array.Divide_Array()
    print "Question 2:"
    ans_Q2 = divide_array_answer.generate_divided_array()
    print ans_Q2
    

    #Question 3
    select_array_elements_answer = select_array_elements.Select_Elements()
    print "Question 3:"
    ansQ3 = select_array_elements_answer.select_elements()
    print ansQ3

    #Question 4
    print "Question 4:"
    print "Please wait for the picture to be generated..."
    N = 1000 # decide the resolution of the mask
    mask_array_answer = mandelbrot.generate_mask_array(N)
    plt.imshow(mask_array_answer.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png') 
    print "The mandelbrot.png is generated successfully and stored under the current directory, thank you for trying the program"


    

if __name__ == "__main__":
    try:
        generate_answe()    

    except KeyboardInterrupt:
        print "the program has been interrupted by KeyboardInterrupt, thanks for trying,Goodbye"
    except EOFError:
        print "the program has been interrupted by EOFERROR, thanks for trying, Goodbye"
    except TypeError:
        print "the program has been interrupted by TypeError, thanks for trying, Goodbye"




