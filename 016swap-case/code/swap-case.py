# You are given a string and your task is to swap cases. 
# Convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    inv = ""
    for i in s:
        if i.isupper() == True:
            inv += i.lower()
        elif i.islower() == True:
            inv += i.upper()
        else:
            inv += i
    return inv

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)