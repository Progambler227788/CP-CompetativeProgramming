def solve(n,array):
    countOdds = 0
    for i in array:
        if i & 1:
            countOdds +=1
    if countOdds & 1:
       return "NO"
    return "YES"



for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    print(solve(n,array))