import math
from collections import defaultdict
for _ in range(int(input())):
    string = input()
    # N U H C A L I O
    data = 'NUHCALIO'
    took = True
    if any(char not in data for char in string):
        took = False
    if took:
        # C A L I C O
        counts = defaultdict(int)
        for i in string:
            if i in ('N','U','C'):
                counts['C']+=1
            elif i =='I' or i =='H':
                counts['I']+=1
            else:
                counts[i]+=1
                # 2//2 -> 1
        counts['C'] = math.ceil(counts['C']/2)
        print(max(counts.values()))
    else:
        print(-1)