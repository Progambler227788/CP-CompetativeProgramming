def solve(array):
    smallestDiff = float('inf')
    element = array[0]
    for i in array[1::]:
        smallestDiff = min( smallestDiff, i - element)
        element = i 
    if smallestDiff < 0:
       return 0
    return smallestDiff//2 + 1

for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    print(solve(array))