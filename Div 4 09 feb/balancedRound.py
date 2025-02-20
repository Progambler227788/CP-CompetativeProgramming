for _ in range(int(input())):
    n,k = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    maxCount = 1
    count = 1
    for i in range(1,n):
        diff = abs( array[i-1] - array[i] ) 
        if diff <=k:
           count+=1
        else:
           maxCount = max(count,maxCount)
           count=1
    maxCount = max(count,maxCount)
        
    print(n-maxCount)
    
    
    
    # 3 4 5 6 10 12
    # 1 2 3