
def giveOutput(n):
    if n==1:
        print(n)
        return
    while n>0:
        print(n,end=" ")
        if n==1 or n<=0:
           break
        if n%2==0:
           n//=2
        else:
          n = (n*3) + 1  
        
n = int(input())
giveOutput(n)