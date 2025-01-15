# import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')
 
# from collections import defaultdict
from collections import Counter
for _ in range(int(input())):
    n,k = map(int, input().split())
    # use string as less collisions
    array = list( input().split())
    
    if k>=n:
        print(1)
    else:
        freq_count = Counter(array)
        
        # onlyKeys = sorted(freq_count.values())
       
        rem = len(freq_count)
 
        
        # 3 2 1
        for i in sorted(freq_count.values()):
            if i<=k:
                rem-=1
                k-=i
        # print(freq_count)
            
        print(rem)
     
            