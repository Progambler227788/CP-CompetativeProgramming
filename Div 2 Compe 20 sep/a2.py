# import sys
# sys.stdout = open('D:/CP/output.txt','w')  
# sys.stdin = open('D:/CP/input.txt','r')

import math
def solveIt(fighters,battles,powers):
    picked = powers[-1]
    # skipping last one
    checking = powers[0: len(powers) - 1]
    while battles>0:
          minimum = min(checking)
          minimumIndex = checking.index(minimum)
          maximum = max(checking)
          maximumIndex = checking.index(maximum)
          

    

    

for _ in range(int (input())):
    n= int(input())
    array = list(map(int, input().split()))
    total_sum = sum(array)
    max_rating = max(array)
    rest_sum = total_sum - max_rating
    # Maximum preserved rating for the last fighter
    # Make sure the final value is non-negative
    result = max(2 * max_rating - total_sum, total_sum - 2 * rest_sum)
    print(result)
    # array,y = map(int, input().split())
    # print(solveIt(x,y,n))

    # string = input()
 
