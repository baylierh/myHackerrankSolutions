# You are given a string and your task is to swap cases. 
# Convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    inv = ""                        #create an empty string
    for i in s:
        if i.isupper() == True:     #if the ith letter in s is uppercase
            inv += i.lower()        #add the lowercase version of it to inv
        elif i.islower() == True:   #if the ith letter in s is lowercase
            inv += i.upper()        #add the uppercase version of it to inv
        else:
            inv += i                #add the ith element to inv if it isn't a letter
    return inv

if __name__ == '__main__':
    # Ask for input
    s = input()
    # Swap the cases!
    result = swap_case(s)
    # Print it out
    print(result)