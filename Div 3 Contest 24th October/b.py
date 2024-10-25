# import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')
def solve(n,array):
    operations = 0
    # check neighbours
    
    
    for i in range(1, n):
        # print(i)
        if  array[n-i-1] != array[i]:
            fetch = array[n-i-1]
            
            # before swap
            # 1 1 2 2
            # current is 2
            # after is 0
            current = int(array[i-1] == array[i]) + int(array[n-i-1] == array[n-i])
            # after swap
            after = int(array[i-1] == array[n-i-1]) + int(array[n-i-1] == array[i])

            if after < current:
               array[i], array[n-i-1] = fetch, array[i]

    for i in range(0 , n-1 ):
        operations+= int(array[i] == array[i+1])
    print(operations)

for _ in range(int(input())):
    n = int(input())
    array = list( map(int,input().split()) )
    solve(n,array)
            

# 1 1 1 1 2 2 2 2