# import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')

# def solve():
#     pass

for _ in range(int(input())):
    # n = int(input())
    # array = list(map(int,input().split()))
    
    # n -> pads , 2-100
    # 2 , 1,2 --- 1
    # 3, 3,1 
    n,a,b = map(int,input().split())
    
    print("NO" if abs(a-b) & 1 else "YES")
