n = int(input("Pick an integer: "))
if n % 2 == 0:
    #continues if n is even
    if n in range(2, 6):    #n is 2, 4, 5
        print("Not Weird")
            
    if n in range(6, 21):   #n is 6, 7,...,20
         print("Weird")
            
    if n > 20:              #n is > 20
        print("Not Weird")
            
    #will excuse the else if n is odd
else:
    print("Weird") 
