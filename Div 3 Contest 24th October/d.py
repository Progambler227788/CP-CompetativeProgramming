def solve(array,n):
    # skipped = set()
    count = 0
    if array.count(0) == n:
        print(n)
        return
    # def check(i,j,skipped):
    #     for m in range(i,j):
    #         if m in skipped:
    #             return False
    #     return True
    
    i = 0  
    while i < n-1:
       
        sum_up = array[i]
        if sum_up == 0:
            count+=1
            # print(i)
            i = i+1
            # print('Skipped')
            continue
        j = i + 1
        check = False

        while j < n:
            # print(j)
            if array[j] == 0:
               count+=1
               i = j +1
               check = True
               j = n
               break

            sum_up+= array[j]
            
            if sum_up == 0:
                count+=1
                i = j + 1
                check = True
                j = n # break while loop
                break
            j+=1
        if not check:
           i+=1
    if array[-1] == 0:
        count+=1
        
    print(count)

for _ in range(int(input())):
    n = int(input())
    array = list(  map(int,input().split()))
    solve(array,n)