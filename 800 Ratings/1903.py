def makeItSortn(n,array,k):
    for repeat in range(n):
      for i in range(1,n):
        array[i:i+k] = sorted(array[i:i+k])
        array[i-1:i+k-1] = sorted(array[i-1:i+k-1])
    for i in range(1,len(array)):
        if array[i-1]> array[i]:
           return "NO"
    return "YES"


for _ in range(int(input())):
    n,k = map(int, input().split())
    array = list( map(int, input().split()) )
    print(makeItSortn(n,array,k))


    # 2 3 1
    # 2 3 1
    # 2 3 1
    # 2 1 3