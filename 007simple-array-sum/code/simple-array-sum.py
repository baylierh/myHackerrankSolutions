# Given an array of integers, find the sum of its elements.
# Array [1, 2, 3] should return 6 (1 + 2 + 3)

def simpleArraySum(ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

