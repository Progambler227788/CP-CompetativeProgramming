def miniMizeIt(array):
    # last pa 5 or start m 2 ,5-2 is 3

    # print( max(array) - min(array))
    if len(array)==1:
       return 0
    ap = array[-1] - array[0]

    for i in range(len(array)-1):
      ap = min(ap, array[i+1]  - array[i])
    print(ap)




for _ in range(int (input())):
    n= int(input())
    array = list(map(int, input().split()))
    miniMizeIt(array)