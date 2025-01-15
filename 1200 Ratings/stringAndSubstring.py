for _ in range(int(input())):
    a = input()
    b = input()
    a1,b1 = {}, {}
    
    # handling abc, cba 
    # abcba would be best as order matters
    for i in a:
        if i in a1:
           a1[i]+=1
        else:
            a1[i] = 1
    total = len(a)
    for i in b:
        if i in b1:
           b1[i]+=1
        else:
            b1[i] = 1
    for key,value in b1.items():
        if key not in a1:
            total += value
        elif a1[key]< value:
            diff = value - a1[key]
            total += diff
    print(total)
           