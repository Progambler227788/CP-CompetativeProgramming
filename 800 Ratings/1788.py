# 1*2*3 = 6

def solve(array,n):
    k=-1
    product = array[0]
    for i in range(1,n):
        product*=array[i]
    j = array[0]
    for i in range(1,n):
        # 2 1 2 , -> 4
        # 2 1 2
        if product//j == j:
           k = i
           break
        j*=array[i]
        # print(j)

    print(k)
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    solve(array,n) 

''' 

6
2 2 1 2 1 2

16, 2
8 , 4
2 , 

2*2
'''