for _ in range(int(input())):
   n = int(input())
   data = input()
   if data[0]!='M' or data[-1]!='T':
      print("NO")
      continue
   yes  = "YES"
   i = 0
   
   while i<n-2:
       if data[i] == 'M':
          i+=1
          while i<n-1:
                if ( data[i]=='I' and data[i+1]!='T' ) or (data[i]!='I' and data[i]!='M'):
                    yes = "NO"
                    i = n
                    break
                if data[i]=='M':
                     i-=1
                     break
                i+=2
       else:
           yes = "NO"
           break
       i+=1
                     
                
          
     
    #  for j in range(i,n-1,2):
    #    # IT,IT
    #    if data[i]=='I' and data[i+1]=='T':
    #        pass
    #    elif data[i]=='M':
    #        yes = "NO"
    #        break
  
   print(yes)
           
    
          
       
   