# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with 
#  the element type float.

import numpy as np

def arrays(arr):
    arr.reverse()
    new_arr = np.array(arr, float)
    return new_arr

arr = input("Enter you array with each entry separated by spaces: ").strip().split(' ')
result = arrays(arr)
print(result)