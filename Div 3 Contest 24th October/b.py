# import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')
def solve(n,array):
    operations = 0
    for m in range(n):
       for i in range(0,n-1):
        if array[i] == array[i+1]:
            # print(i,i+1,n-i-1)
            fetch = array[n-i-1]
            # print(n-i-1,i)
            if fetch!= array[i]: # swap the elements
             if n-i<n and n-i-2>=0 and n-i-2<n and array[i] == array[n-i] and array[i]==array[n-i-2]:
                continue
             array[i], array[n-i-1] = fetch, array[i]
    # print(array)

    # 
    for i in range(0 , n-1 ):
        if array[i] == array[i+1]:
            operations+=1
    print(operations)

for _ in range(int(input())):
    n = int(input())
    array = list( map(int,input().split()) )
    solve(n,array)
            

# 1 1 1 1