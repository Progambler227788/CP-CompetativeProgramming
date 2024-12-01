for _ in range(int(input())):
    n,m = map(int,input().split())
    maping = []
    for _ in range(int(n)):
        string = input()
        count = 0
        for i in string:
            if i == '#':
                count+=1
        if count!=0:
          maping.append(count)
    # print(maping)
    check = True
    
    for m in range( 1, len(maping )):
        if maping[m-1] != maping[m]:
            check = False
            break
    if check:
        print("ferb ")
    else:
        print("phineas")
        