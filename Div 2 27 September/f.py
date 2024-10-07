
import math

# agr maximum multiple times ara h tu agr even index hua tu ceil use krna h

# lol, i got this edge case by running with array of size 9 as 1 2 3 5 5 5 5 5 so I got it issue

def checkIndex(array,element,n):
    for i in range( n ):
        if array[i] == element and i%2==0:
           return False
    return True


def checkOcurrence(array,element,n):
    count=0
    previous = 0
    for i in range( n ):
        if array[i] == element and previous+1!=i:
            count+=1
            previous = i
    return count

def takeMinimum(array,n):
    minimum = float('inf')
    for i in range(1, n, 2):
        if array[i] < minimum:
            minimum = array[i]
    return minimum



def takeMinimumEven(array,n):
    minimum = float('inf')
    for i in range(0, n, 2):
        if array[i] < minimum:
            minimum = array[i]
    return minimum
def solve(array,n):
    takeMax = max(array)
    # if array.index(takeMax) % 2 != 0 and n%2!=0:
    #    takeSorted = sorted()
    

    # 1 2 3 4 4 5 3
    # 2,4,5 -> 5+2 -> 7
    # 1,3,4,3 -> 4+1 -> 5
    stored = checkOcurrence(array,takeMax,n)
    if stored >1:
       return takeMax*stored + stored
        
    if n & 1 and checkIndex(array,takeMax,n) :
        return takeMax + math.floor(n/2) + takeMinimum(array,n) # odd case
    if checkIndex(array,takeMax,n): # odd case
        return takeMax + math.ceil(n/2) + takeMinimum(array,n)

    # 1 2 3 4
    # 2,4 -> even minimum
    # 1 2 4 3
    # 1 2 4 3 -> odd minimum, maximum at odd then odd will be minimum
    # print('hello')
    # print(takeMinimumEven(array,n))
    return takeMax + math.ceil(n/2) + takeMinimumEven(array,n)

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