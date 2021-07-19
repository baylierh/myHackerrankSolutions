# Given the participants' score sheet for your University
# Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    first = 0
    second = 0
    for i in range(n):
        if arr[i] > first:
            first = arr[i]
    for i in range(n):
        if arr[i] < first:
            if arr[i] > second:
                second = arr[i]
    print(first)
    print(second)