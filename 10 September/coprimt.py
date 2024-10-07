# import sys
# sys.stdout = open('D:/CP/10 SEPTEMBER/output.txt','w')
# sys.stdin = open('D:/CP/10 SEPTEMBER/input.txt','r')

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def makeUniqueMap(array):
    maping = {}
    n = len(array)
    for index in range(n-1, -1, -1  ):
        if array[index] not in maping:
           maping[array[index]] = index
        else:
            if index > maping[array[index]]:
               maping[array[index]] = index
    maximum = -1
    for i in range( 1, 1001):
        for j in range(i, -1, -1):
            if gcd(i,j) == 1 and i in maping and j in maping:
               maximum = max(maximum, maping[i] + maping[j] )
    return maximum if maximum==-1 else maximum+2 # +2 as 1 based numbering



              

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    maxIandJ = -1
    print(makeUniqueMap(array))
    # for j in range( n-1, -1, -1):
    #     for i in range(j , -1, -1):
    #         if gcd(array[i], array[j]) == 1 and i+ j > maxIandJ:
    #            maxIandJ = i+j
    #         else:
    #            i=-1
    # if maxIandJ != -1:
    #    print(maxIandJ+2)
    # else:
    #    print(maxIandJ)

# 1 2 3

# 3+2
# 3+1
# 2+2
# 2+1