# Given an array of integers, find the sum of its elements.
# Array [1, 2, 3] should return 6 (1 + 2 + 3)

# simpleArraySum takes an array as input and adds each element
#  of it to the variable "sum" which is returned at the end
def simpleArraySum(ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

# fixArrayInput takes an array that is in string form
# (ex: 1 2 3) and turns it into a list of integers
def fixArrayInput(ar):          #ar --> "1 2"
    new_ar = []                 #Empty list created
    for i in ar.split():        #ar.split() --> ["1", "2"]
        new_ar.append(int(i))   
    return new_ar               #new_ar --> [1, 2]
     

print("Find the sum of an array's elements!")
print("Separate each element with a space like so: 1 2 3")

# Ask for input
ar = input("Enter the array: ")

# 'Fix' the input so simpleArraySum() can work with it
fixed_ar = fixArrayInput(ar)

# Give the fixed array to simpleArraySum and print the result!
print("Sum:", simpleArraySum(fixed_ar))