# Given an array of integers, find the sum of its elements.
# Array [1, 2, 3] should return 6 (1 + 2 + 3)

def simpleArraySum(ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

def fixArrayInput(ar):
    new_ar = []
    for i in ar.split():
        new_ar.append(int(i))
    return new_ar
     

print("Find the sum of an array's entries!")
print("(Separate each entry with a space like so: 1 2 3)")

ar = input("Enter the array: ")

fixed_ar = fixArrayInput(ar)

print(simpleArraySum(fixed_ar))