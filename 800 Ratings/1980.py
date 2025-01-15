from collections import defaultdict
for _ in range(int(input())):
    n,rounds = map(int , input().split())
    problems = input()
    freq = defaultdict(int)
    check = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    for i in check:
        freq[i] = 0
    for i in problems:
        freq[i]+=1
        
    total = 0

    for f in freq.values():
        # print(f)
        if f == 0:
            total += rounds
            # print('helo')
        elif f<rounds:
             diff = rounds - f
             total+=diff
    print(total)
          
        
        
    # print(freq)
    
    # print(sum(freq.values()))
    

    
    