# from collections import defaultdict
for _ in range(int(input())):
    
    dp = set()
    rem = set()
    n = int(input())
    count = 1
    for num in range(1,100):
        if count == n+1:
           break
        o = num%count
        if o not in rem:
           rem.add(o)
           dp.add( num )
           count+=1
    print(*dp)
        