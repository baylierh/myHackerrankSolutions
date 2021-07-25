# You are given a string. Split the string on a " " (space)
#  delimiter and join using a - hyphen.

# split_and_join() splits a string apart anywhere there is
#  a space. Then it cycles through the new list created
#  to piece together a new string with hypens where
#  there used to be spaces.
def split_and_join(line):
    line = line.split(" ")
    new = ""
    count = 0
    for i in line:                  #cycle through the list of words
        if count != len(line) - 1:  #if it isn't the last word...
            new = new + i + "-"     #add it to "new" and add a hyphen
            count += 1
        else:                       #if it is the last word...
            new = new + i           #just add it to "new" without adding a hyphen
    return new

if __name__ == '__main__':
    #Ask for input
    line = input("Enter a phrase: ")
    #Use the function on the input
    result = split_and_join(line)
    #Print out the result
    print(result)