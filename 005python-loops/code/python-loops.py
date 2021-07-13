#Ask for input; change to an integer
n = int(input("Enter an integer: "))

#List of integers less than n (non-negative)
less_n = range(0, n)

#Print the square of every number in the list
for i in less_n:
    print(i**2)