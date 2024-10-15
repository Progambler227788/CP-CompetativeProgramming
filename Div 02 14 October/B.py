# 3 2

# 3 1 2

# 3 2 1
# at most 1

# if x is 1:
#    sum of array

# suming then dividing by x
import math
def solve(n,x,array):
    # rem = 0
    # if x>n:
    #     x = n    
    # data = sorted(array, reverse= True)
    # done = 0
    print(   max(  max(array) , int(math.ceil( sum(array) / x ))))

for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    solve(n,x,arr)



''' 
3 2
3 1 2
1
3 2 1

1 1

2 1 1

1 1

1 0 1
'''