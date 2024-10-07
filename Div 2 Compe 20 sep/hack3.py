from math import gcd
from collections import defaultdict
import sys
sys.stdout = open('output.txt','w')  
sys.stdin = open('input.txt','r')
import random
def solve(n,ants):
    n = len(ants)
    if n <= 2:
        return 0  # All are already collinear

    # Randomly choose a point as the pivot
    pivot_index = random.randint(0, n - 1)
    pivot = ants[pivot_index]
    
    slopes = defaultdict(int)

    for i in range(n):
        if i != pivot_index:
            deltaY = ants[i][1] - pivot[1]
            deltaX = ants[i][0] - pivot[0]
            g = gcd(deltaX, deltaY)
            deltaX //= g
            deltaY //= g
        
            if deltaX == 0:
                    deltaX, deltaY = deltaX+1, deltaX
             
            elif deltaY == 0:
                deltaX, deltaY = deltaY, deltaY+1

            slopes[(deltaX, deltaY)] += 1
    
    max_collinear = max(slopes.values(), default=0) + 1
    return n - max_collinear
for i in range(int(input())):
    n = int(input())
    ants = [tuple(map(int, input().split())) for _ in range(n)]
    print(f"Case #{i+1}: {solve(n,ants)}")
     
    