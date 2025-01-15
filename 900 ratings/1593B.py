
def solve(a,b):
    # b will be either 25,50,75,00
    aLen = len(a) - 1
    index = aLen
    skipped = 0
    while index>=0 and a[index]!=b[1]:
        skipped+=1
        index-=1
        
    index-=1 # because we need to move further towards first character 
    if index<0:
       return float('inf')
   
    while index>=0 and a[index]!=b[0]:
        skipped+=1
        index-=1
        
    return float('inf') if index<0 else skipped
    

data = ["00","25","75","50"]      
for _ in range(int(input())):
    n  = input()
    sab_se_kam = float('inf')
    for i in data:
         sab_se_kam = min(solve(n,i),sab_se_kam)
    print( sab_se_kam)
    