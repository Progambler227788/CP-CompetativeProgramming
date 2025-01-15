for _ in range(int(input())):
    n,a,b,c = map(int, input().split())
    count = 3
    data = [a,b,c]
    total = a+b+c
    if total==n:
       count = 3
       print(count)
    elif total>n:
        if a>=n:
             count = 1
        elif b>=n:
             count = 2
        elif c>=n:
             count = 3
        print(count)
    else:
        print('here')
        while total<n:
              total*=2
              count+=3
        # k = -2
        # while total>n:
        #       total-= data[k]
        #       k+=1
        #       if k == 0:
        #          k = -2
        #       count-=1
        print(count+1)
        
    
               
       
    