# Given an integer, n, and n space-separated integers as 
#  input, create a tuple, t, of those  integers.
# Then compute and print the result of hash(t).

# fixArrayInput takes an array that is in string form
# (ex: 1 2 3) and turns it into a list of integers
def fixArrayInput(ar):
    new_ar = []
    for i in ar.split():
        new_ar.append(int(i))
    return new_ar

# Ask for input
integer_list = input("Enter a list of integers separated by spaces: ")

# Format the list/array
fixed_list = fixArrayInput(integer_list)

# Change the type from a list to a tuple
t = tuple(fixed_list)

print("Hash of input: ", hash(t))
