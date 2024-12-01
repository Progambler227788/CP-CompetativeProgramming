from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    array = list( map(int,input().split()))
    frequencies = defaultdict(int)
    totalDollars = 0
    for i in array:
        totalDollars +=  (i / n)
        frequencies[i]+=1 
    # print(totalDollars)
    # print(frequencies)
    remainingDollars = 10**9
    miniI = n
    for i in array:
        calc = totalDollars - ( (i *  frequencies[i]  )  / n )
        if calc < remainingDollars:
            # print(calc,i)
            miniI = i
            remainingDollars = calc
    print(miniI)
    
    
        