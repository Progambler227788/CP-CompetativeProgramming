def canSort(array):
    # for n in range(len(array)):
    #   for i in range(1,len(array)-1):
    #     if array[i-1] < array[i] and array[i] > array[i+1]:
    #        array[i], array[i+1] = array[i+1], array[i]
    # if array == sorted(array):
    #    return "YES"
    # return "NO"

    if array[0]== 1:
       return "YES"
    return "NO"

for _ in range(int(input())):
    n = int(input())
    array = list(map( int, input().split()  ))
    print( canSort(array))