#Make a function called is_leap with year as an input
def is_leap(year):
    #Set the default of leap to False
    leap = False
    
    #Can be divided by 4 evenly? It's a leap year!
    if year % 4 == 0: 
        leap = True
    
        #Unless...evenly divisible by 100 - NOT a leap!
        if year % 100 == 0:
            leap = False

            #Unless..evenly div. by 400 - Is a leap!
            if year % 400 == 0:
                leap = True

    #True or False will be returned when is_leap is called
    return leap

#Ask for year input
year = int(input())

#Print whatever is_leap returns
print(is_leap(year))