# Given the participants' score sheet for your University
# Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    # Ask for the number of scores
    n = int(input())
    # Ask for the scores separated by spaces
    arr = list(map(int, input().split()))
    #print(arr)
    # Intialize the variables first and second
    first = 0
    second = 0
    # Make a loop that will cycle through the list
    #  to fin the highest score
    for i in range(n):
        if arr[i] > first:
            first = arr[i]
    # Make a loop that will find the second highest score
    for i in range(n):
        if arr[i] < first:
            if arr[i] > second:
                second = arr[i]
    #print(first)
    # Print out the second highest score!
    print("The second highest score is...", second)