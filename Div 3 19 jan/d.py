for _ in range(int(input())):
    n = int(input())
    array = list( map(int, input().split()))
    check = 0
    for i in range(n-1):
        if array[i]>array[i+1]:
            check = 1
            break
        else:
            # do operation
            array[i+1]-=array[i]
            array[i] = 0
    print("NO" if check==1 else "YES")
    
        
            
           