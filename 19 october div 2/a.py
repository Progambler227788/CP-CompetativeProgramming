def solve(array,n):
    # take = max(array)
    # index = array.index(take)
    # array[0],array[index] = array[index] , array[0]
    # 7 6 5
    maxA = max(array)
    minA = min(array)
    print( (maxA - minA) * (n-1))


for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    solve(array,n)
    
