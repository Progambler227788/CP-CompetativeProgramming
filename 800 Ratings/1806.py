import sys
import math
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')

def solve(a,b,c,d):
    ''' 
    0 0 4 5
if d < b:
   impossible
3 0  4  0
if d==b and a < c: 
   impossible
if a==c and b==d:
   zero moves
'''

# 0 -2 -3 3
# 5  3 -3 3 -> 5 done
# 
    if  d < b or (d==b and a<c):
      return  -1
    if a==c and b==d:
       return 0
    # -1, 3 -> 4
    distance = 0
    # 0 0 4 5
    if b <0 and d>0 : 
        distance = abs(b)  + d
    else:
       # -1,-3 -> 2 , 1,3 -> 2 
       distance = abs (abs(b) - abs(d))
   
    # -3, -1 -> 2
    #  1   3 -> 2

    # -1 0 -1 2
    # -1 2 -1 2
    moves = distance + a 
    # print(moves)
    if moves == c:
       return distance
    
    if moves < c:
       return - 1  # -5,2,2,4 -> -3,4,2,4, can't move a now
 
    if moves<0 and c>0:
       # 2,-2 is 4
       # 
       return distance +  abs(moves)  + c
    
    if moves>0 and c<0:
       return distance +  moves  + abs(c)
       
    
    return distance + ( abs( abs(moves)  -  abs(c )  ) )

for _ in range(int(input())):
   a,b,c,d = map(int, input().split())
   print(solve(a,b,c,d))
