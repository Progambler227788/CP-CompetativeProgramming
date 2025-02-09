for _ in range(int(input())):
    a1,a2,a4,a5 = map(int , input().split())
    a3 = a4 - a2
    count0 = 0
    if a3 == a1+a2:
        count0+=1
    if a4 == a3+a2:
        count0+=1
    if a5 == a4+a3:
        count0+=1
    a3 = a1 + a2
    count1 = 0
    if a3 == a1+a2:
        count1+=1
    if a4 == a3+a2:
        count1+=1
    if a5 == a4+a3:
        count1+=1
    count2 = 0
    a3 = a5 - a4
    if a3 == a1+a2:
        count2+=1
    if a4 == a3+a2:
        count2+=1
    if a5 == a4+a3:
        count2+=1
    print(max(count0,count1,count2))