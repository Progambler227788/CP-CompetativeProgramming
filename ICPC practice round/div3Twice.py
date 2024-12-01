from collections import defaultdict
import math
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    data  = defaultdict(int)
    for i in array:
        data[i]+=1
    count = 0
    for f in data.values():
        count+=   math.floor(f//2)
    print(count)
        