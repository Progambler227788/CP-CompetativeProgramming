# import sys
# sys.stdout = open('D:/CP/output.txt','w')  
# sys.stdin = open('D:/CP/input.txt','r')
#NOTE:
# Ignore above lines that are meant to be manual testing on IDE via files
def lukesEatingPiles(piles,size,x):

    # |element - affinity| <= x.... affinity is also element from an array initially set to any number


    ranges = {}
    for index,pile in enumerate(piles):
        first = pile - x if pile-x>=0 else 0
        second = pile + x
        ranges[ index ] = (first, second)

    left = ranges[0][0]
    right = ranges[0][1]
    count = 0
    for key in range(1,size):
        if ranges[key][0] > right or ranges[key][1] < left:
           count+=1
           left = ranges[key][0] 
           right = ranges[key][1]
        left = max(left,ranges[key][0] )
        right = min( right, ranges[key][1])
        
    print(count)

   

    #********************INVENTORY****************

testCases = int(input())
# read test cases 
for t in range(testCases):
    taken = input()
    bogambo = taken.split()
    size = int(bogambo[0])
    x = int(bogambo[1])
    inputArray =input()
    inputArray = inputArray.split()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    lukesEatingPiles(inputArray,size,x)


    
    
