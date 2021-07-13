# Calculate and print the sum of the elements in an array
# Some of those integers may be quite large

# aVeryBigSum takes an array as input and adds each element
#  of it to the variable "sum" which is returned at the end
def aVeryBigSum(ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

# fixArrayInput takes an array that is in string form
# (ex: 10001 10002 10003) and turns it into a list of integers
def fixArrayInput(ar):
    new_ar = []
    for i in ar.split():
        new_ar.append(int(i))
    return new_ar

print("Find the sum of an array's elements!")
print("Even works with large integers!")
print("Separate each element with a space like so: 1000001 1000002")

# Ask for input
ar = input("Enter the array: ")

# 'Fix' the input so simpleArraySum() can work with it
fixed_ar = fixArrayInput(ar)

# Give the fixed array to simpleArraySum and print the result!
print("Sum:", aVeryBigSum(fixed_ar))
