def solve(n, array):
    maxFrequency = 0
    counter = 1
    if array[0] == 0:
        maxFrequency = 1
    for index in range(1,n):
        if array[index-1] == array[index] == 0:
            counter+=1
            maxFrequency = max(maxFrequency, counter)
        elif array[index] == 0:
            counter = 1
            maxFrequency = max(maxFrequency, counter)
    return maxFrequency

for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    print(solve(n,array))

