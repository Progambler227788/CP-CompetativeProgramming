from collections import defaultdict
for _ in range(int(input())):
    n,k = map(int, input().split())
    array = list(input().split())
    # a+b=k, k-b
    # print(array)
    maping = defaultdict(int)
    count = 0
    
    for i in array:
        m = str(k - int(i))
        
        if maping[m] > 0:
           maping[m]-=1
           count+=1
        else:
          maping[i]+=1
        # print(maping)
        
    print(count)
           