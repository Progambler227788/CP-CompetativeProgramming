import sys
sys.stdout = open('output.txt','w')  
sys.stdin =  open('input.txt','r')
from collections import defaultdict
def factors(number):
    n=int(number**.5)+1
    x=number
    divisors=[]
    visited =[1] * n
    primes=[]
    for p in range(2, n):
        if visited[p]:
            primes.append(p)

            while x%p==0:
                x//=p
                divisors.append(p)
            # print(p)
            for i in range(p*p, n, p):
                visited[i] = False
    if x!=1:
        divisors.append(x) 
    # # print(divisors)
    # newDivisors = defaultdict(int)
    # for i in divisors:
    #     newDivisors[i]+=1
    # data = []
    # for key,value in newDivisors.items():
    #     data.append( ( key**value) )
    # print(data)
    return divisors
def solve(number):
    taken = factors(number)
    total = sum(taken)
    # print(total)
    if total > 41:
       return -1
    elif total==41:
        return taken
    remaining = 41 - total
    taken.extend( [1] * remaining)
    # print(taken)
    if len(taken)>100:
        return -1
    return taken
for _ in range(int(input())):
   output = solve(int(input()))
   if output!=-1:
       size = len(output)
       print(  f"Case #{_+1}: {size}",*output) 
   else:
       print(  f"Case #{_+1}: {-1}") 
       

