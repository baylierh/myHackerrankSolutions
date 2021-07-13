# Given an integer, n, and n space-separated integers as 
#  input, create a tuple, t, of those  integers.
# Then compute and print the result of hash(t).

integer_list = input("Enter list of integers separated with spaces: ")

t = tuple(integer_list)

print(hash(t))
