

def giveCost(a,b):
    y = "YES"
    n = "NO"
    if a==1 and b==0 or (b==1 and a==0):
       return n
    
    if a%2==0 and b%2==0:
       return y
    
    if a>0 and b==0:
       if a%2==0:
          return y
       else:
          return n
    if b>0 and a==0:
       if b%2==0:
          return y
       else:
          return n
       
    if a%2!=0 and b%2!=0:
       return n
    
    if a%2==0 and b%2!=0:
       return y
    return n
   
             
            

for _ in range(int(input())):
   n,k = map(int, input().split())
   print(giveCost(n,k))
   