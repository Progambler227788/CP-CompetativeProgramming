for _ in range(int(input())):
    x,y= map(int, input().split())
   
    output = "YES"
    
    if ( (x+1-y ) %9 == 0 ) and (x+1>=y):
        output="YES"
    else:
         output="NO"
      
    print(output)
    
    
    
    # 4 4
                