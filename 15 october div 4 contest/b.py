
for _ in range(int(input())):
  m,a,b,c = map(int , input().split())
  total=0
  rem = m + m
  if m>=a:
      total += a
      rem-=a
  elif m<a:
      total += m
      rem -= m 
      
  if m>=b:
      total += b
      rem-=b
  elif m<b:
      total += m
      rem -= m 
  
  if c>rem:
      total+=rem
  else:
      total+=c
  print(total) 
  
  
     
                
    
    