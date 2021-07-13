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

integer_list = input("Enter list of integers separated with spaces: ")

fixed_list = fixArrayInput(integer_list)
print(fixed_list)

t = tuple(fixed_list)
print(t)

print(hash(t))
