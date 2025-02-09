for _ in range(int(input())):
    n, m = map(int,input().split())
    data = []
    check = 0
    for i in range(n):
        tempi = sorted(list(map(int,input().split())))
        # 0 2 4
        for i in range(1,m):
            if tempi[i] - tempi[i-1] !=n:
                check = 1
                break
        data.append(tempi)
        
    # 1 2 0 3
    if check == 1:
        print(-1)
        continue
    
    new = []
    for k in range(n):
        # print(data[k][0])
        new.append( (data[k][0],k+1))
    # print(new)
    new = sorted(new , key = lambda x:x[0])
    
    p = []
    for i,j in new:
        p.append(j)
    print(*p)
        
        
            
               
                
        