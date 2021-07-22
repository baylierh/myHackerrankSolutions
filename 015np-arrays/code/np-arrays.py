# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with 
#  the element type float.

# Import numpy
import numpy as np

# Creat the array() function that takes a list 
#  with space separated entries
def arrays(arr):
    arr.reverse()                   #reverse the given list
    new_arr = np.array(arr, float)  #create new float np array
    return new_arr

# Ask for input
arr = input("Enter you array with each entry separated by spaces: ").strip().split(' ')

# Let arrays() return the reverse float version of the list
result = arrays(arr)
print(result)