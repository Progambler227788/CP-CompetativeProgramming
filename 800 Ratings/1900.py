def solve(n,array):
    count = 0
    i = 0
    while i < n:
        consectives = 0
        while i<n and array[i] == '.':
              consectives+=1
              i+=1
    
        if consectives>=3:
           return 2
        else:
            count+=consectives
        i+=1
    return count

for _ in range(int(input())):
    n = int(input())
    array = input()
    print(solve(n,array))

