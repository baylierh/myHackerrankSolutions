# Compute the the average
# Average = Sum of Distinct Heights / Total # of Dis. Heights
# Hint: use the built-in round() function

# Average function should take an array as input
#  and returns the average of the array's elements
#  rounded to 3 places after the decimal
# Uses sets instead of lists
def average(arr):
    set_arr = set(arr)
    avg = sum(set_arr) / len(set_arr)
    rounded = round(avg, 3)
    return rounded

# From a previous code...
# fixArrayInput takes an array that is in string form
# (ex: 1 2 3) and turns it into a list of integers
def fixArrayInput(ar):          #ar --> "1 2"
    new_ar = []                 #Empty list created
    for i in ar.split():        #ar.split() --> ["1", "2"]
        new_ar.append(int(i))   
    return new_ar               #new_ar --> [1, 2]

# Ask for input
inp_arr = input("Enter the values in the array separated by spaces: ")

# 'Fix' the input (turn into a list)
new_arr = fixArrayInput(inp_arr)

# Find the average and print it out!
ans = average(new_arr)
print("Average: ", ans)