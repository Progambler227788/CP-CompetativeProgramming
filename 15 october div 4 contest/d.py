for _ in range(int(input())):
    k,l1,r1,l2,r2 = map(int , input().split())
    
    count = 0
    for x in range (l1,r1+1):
        p = 0
        while True:
            y = k* (x**p)
            if  y > r2:
                break
            if y >=l2:
                count+=1
            p+=1
            
    print(count)
                
            
        