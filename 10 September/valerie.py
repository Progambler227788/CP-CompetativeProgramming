def giveYesOrNo(data):
    maping = []
    for i in data:
        if i in maping:
           return 'YES'
        maping.append(i)
    return 'NO'
for _ in range(int(input())):
    size = int(input())
    data = list(map(int,input().split()))
    print(giveYesOrNo(data)) 

# array having two same elements will form same sum in two different sub arrays
# array having all distinct elements will not be able to form same sum