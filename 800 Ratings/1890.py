



from itertools import permutations


def checkAdjacentEqual(arr):
    p = permutations(arr) 
    container = set(list(p))
    for j in container: 
        array = j
        container.remove(array)
        # print(array)
        inner = "YES"
        for element in range( len(j) - 2 ):
           if array[element] + array[element+1] != array[element+1] + array[element+2]:
              inner = "NO"
        if inner=="YES":
           return "YES"
    return "NO"
              
 
for _ in range(int(input())):
    n = int(input())
    array = list(map( int, input().split()  ))
    print( checkAdjacentEqual(array))