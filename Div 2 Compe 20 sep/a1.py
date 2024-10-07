# import sys
# sys.stdout = open('D:/CP/output.txt','w')  
# sys.stdin = open('D:/CP/input.txt','r')

import math
def solveIt(x,y,n):
    # agr 5 fruits ha tu agr x-> 3 ha tu 5/3 b 2 dega or 5-=3 b 2 deyga until 5 zero ni huta , tu jo count huga whi score
    # target value greater after points
    count = 0
    if x < y:
        count+= math.ceil(n / x)
    else:
        count+= math.ceil(n / y)
    return count

    

for _ in range(int (input())):
    n= int(input())
    x,y = map(int, input().split())
    print(solveIt(x,y,n))

    # string = input()
    # array = list(map(int, input().split()))
'''

5 -> total fruits

x < y
n - x
5-3 == 2
 n-=x

6 -> total

4 , 3



3 -> tota; friiots

3 -> put a time
4 -> 1 sec

3, 2 -> 2

3 -> total fruits
1,1,1 -> 2 

6

3,'''