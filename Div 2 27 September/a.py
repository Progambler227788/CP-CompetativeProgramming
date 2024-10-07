
import math

# agr maximum multiple times ara h tu agr even index hua tu ceil use krna h

# lol, i got this edge case by running with array of size 9 as 1 2 3 5 5 5 5 5 so I got it issue

def checkIndex(array,element,n):
    for i in range( n ):
        if array[i] == element and i%2==0:
           return False
    return True

# def takeMinimum(array,n)
def solve(array,n):
    takeMax = max(array)
    # if array.index(takeMax) % 2 != 0 and n%2!=0:
    #    takeSorted = sorted()
    

    # 1 2 3 4 4 5 3
    # 2,4,5 -> 5+2 -> 7
    # 1,3,4,3 -> 4+1 -> 5
    if n & 1 and checkIndex(array,takeMax,n) :

        return takeMax + math.floor(n/2)
    return takeMax + math.ceil(n/2)

for _ in range(int(input())):
    n = int(input())
    array = list(  map(int, input().split()))
    print(solve(array,n))

# Intitutions
''' 
Max at Even Index, size//2 ceil function


4,5,4,4 -> n even, size//2 

4,5,4 -> n odd,
4,5,4,4,3
5,4 == 5 + 2
4,5,4  ,4, 4,4, 4,4 == 8
5,4,4,4 == 5+4 == 9
4,4,4,4 ==
4,4,3
3 + 4 == 7

4 -> 4 , 1
4,4 -> 4, 1
4,5,4 -> 5, 1
4,5,4,4-> 5,4, 2
4,5,4,4,4 -> 5,4, 2
4,5,4,4,4,4 -> 5,4,4, 3

4,4,4 -> 4+3 == 7


1,2,3,4,5 -> 1,3,5
3,2,1   -> 

4,5,4 -> odd index + odd

5+1

'''