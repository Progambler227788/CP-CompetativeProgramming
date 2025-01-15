for _ in range(int(input())):
    a,b,c = map(int , input().split())
    total = a
    
    check = b%3
    rightly = b // 3
    if check == 0:
       total += (rightly)
       
       now = c%3
       yes = c//3
       if now==1 or now ==2:
           total += yes + 1 
       else:
           total += yes
    #    total+=  yes + now         
         
    elif check == 1 or check == 2:
        #  print(check)
         rem = check + c 
         if rem>=3:
            total += (rightly)
            temp = 0
            if c >= check:
                temp = c - (3 - check)
                
            total += 1 # extracted the unis 
            b = ( temp ) // 3
            yes = ( temp ) % 3
            # print(temp)
            # print(b)
            # print(yes)
            
            if yes==1 or yes ==2:
               total += b + 1 
            else:
               total+=b 
               
            # total +=  ( b + yes )
         else:
             total = -1
    print(total)
            
            
        
    