def solve(array,n):
    # skipped = set()
    count = 0
    # if array.count(0) == n:
    #     print(n)
    #     return
    # def check(i,j,skipped):
    #     for m in range(i,j):
    #         if m in skipped:
    #             return False
    #     return True
    
    # i = 0  
    data = set()
    data.add(0)
    sum_up = 0
    for i in range(n):
        sum_up += array[i]
        if sum_up in data:
            count+=1
            sum_up = 0
            data = set()
            # data.add(0)
        data.add(sum_up) 
        # i+=1        
        
    print(count)

for _ in range(int(input())):
    n = int(input())
    array = list(  map(int,input().split()))
    solve(array,n)