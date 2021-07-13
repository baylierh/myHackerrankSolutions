# Calculate and print the sum of the elements in an array
# Some of those integers may be quite large

def aVeryBigSum(ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

def fixArrayInput(ar):
    new_ar = []
    for i in ar.split():
        new_ar.append(int(i))
    return new_ar

print("Find the sum of an array's elements!")
print("Separate each element with a space like so: 1 2 3")

# Ask for input
ar = input("Enter the array: ")

# 'Fix' the input so simpleArraySum() can work with it
fixed_ar = fixArrayInput(ar)

# Give the fixed array to simpleArraySum and print the result!
print("Sum:", aVeryBigSum(fixed_ar))