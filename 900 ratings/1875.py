for _ in range(int(input())):
    
    # find repeated operation decreasing by 1 will be permanent -> repeated operation
    a,b,n = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(n):
        if array[i]>a:
            array[i] = a
            # take total and subtract the -1 at once 
            # b is initial total
    total = (sum(array) - 1) + b 
    
    print(total)
    
    

    