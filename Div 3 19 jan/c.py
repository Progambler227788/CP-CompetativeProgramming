for _ in range(int(input())):
    n,k = map(int, input().split())
    array = list( map(int, input().split()))
    data = {}
    count = 0
    for i in array:
        mm = k - i
        if mm in data:
            count+= 1
            data[mm] = 0
        if i not in data:
            data[i] = 1
        else:
          data[i]+=1
    print(count)