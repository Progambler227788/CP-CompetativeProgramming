
def solvee(arr):
    arr = sorted(arr)
    maxi = arr[0]
    for i in arr[1::]:
        maxi = (maxi + i) >> 1 # divide by 2
    return maxi
    
   

# 1 4 5 7 8
# 1 4 5 



for _ in range( int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solvee(arr))


