
''' 
4//2
-1,-1,1,1

1,-1,-1 -> 2
1,-1,-1,-1 -> 1

total -> odd

1,1,1,-1,-1 if positives > negatives
1,1,1,1,-1,-1,-1 , negatives % 2 is answer
else
-1 -1 -1 1 1
1,1,1,1,1 ->  then count of negatives is answer
1,-1,-1 -> answer is 2

total even ->
1,1,1,1,-1,-1 Positives > negatives 1,1,1,-1 negatives % 2 is answer
-1,-1,-1,1    Negatives> Positives  -1,-1,-1,-1,1,1 count of positives is answer
'''

import sys
import math
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')

def solve(n,array):
    countNegatives = 0
    countPos = 0
    for ele in array:
        if ele ==1:
            countPos+=1
        else:
            countNegatives+=1

    if countNegatives == 0:
        return 0
    
     
    if countPos == countNegatives and countNegatives%2==0:
        return 0
    
    if countPos == countNegatives and countNegatives & 1:
        return 1
    

    # 1 -1 -> 1
    # 1 1 -1 -1 -> 0
    # -1 -1 -> 2//2 is 1 + 1
    
    if countPos > countNegatives and countNegatives & 1:
        return 1 # odd negatives
    
    if countPos > countNegatives and countNegatives % 2 == 0:
        return 0 # even negatives  1 1 1 1 -1 -1
    
    if countNegatives & 1 and countPos == 0:
        # odd case when +ves are zero

        # -1 -1 -1 -> 3//2 is 2 so it is 3 then
        # -1 -1 -1 -1 -> 4//2 is 2 so it is also 3
        # -1 -1 -1 -1 -1 -> 5//3 is 3 so it is 3 returned
        store = math.ceil(n/2)
        if store & 1:
            return store 
        return store + 1
    
    if countPos == 0 and countNegatives%2==0:
        # even case when +ves are zero
        # -1 -1 -> 2,  2//2 is 1 and then 2 returned
        # -1 -1 -1 -1 -> 4//2 is 2
        # -1 -1 -1 -1 -1 -1 -> 6//2 -> 3+1 so 4 is returned
        # -1 -1 -1 -1 -1 -1 -1 -1 -> 8//2 is 4 returned
        # -1 -1  1, -1 -1 -1 1 1
        # -1,-1,-1, 1, 1
        store = countNegatives//2
        # print(store)
        if store & 1:
            return store + 1
        return store
    
    mid = n//2 
    store = countNegatives - mid
    
    if mid & 1: # odd negatvies when pos are not zero

        # atleast negatives half ya half se kam huny chaye
        # 6 is array length and negatives are 3 then 3 
        # odd + 1
        # 6 is array length and negatives are 4 then difference is 1
        # if even length then difference + 1
        # if odd length
        # 5, -1 -1 -1 1 1 -> 5//2 is 2 -> 3-2 is 1
        # 3, -1 ,-1, 1
        # -1 -1 -1  1 -> 1 , 3//2 is 1 
        # -1,-1,1 -> 2
        # -1,-1,-1,-1,1 -> 2
        # -1 -1 -1  -1  -1  1  1 1 1 -> 5
        # store = countNegatives//2
        # if store & 1:
        #     return store 
        return store + 1

    # store = countNegatives//2
    # if store & 1:
    #     return store + 1
    return store
# 3//2 is 1 
    # 
        # return n//2 + 1 # half + 1
        # if n//
        # -1 -1 -1 -> 1 1 1
        # -1 -1 -> 1 1
        # -1 -1 -> 1 1
        # -1 -1 -1 -1 ->  1 1 -1 -1
    # if countPos == 0:
    #     return countNegatives
    # -1, -1, -1, -1, -1 -> 
    # atleast half + 1
    # -1,-1,-1 -> 3/2 -> 
    # -1,-1,-1,-1 -> 2
    # -1,-1,-1,-1,-1 -> 3
    # -1,-1,-1,-1,-1,-1 -> 4
    # -1, -1 -> 2
    # -1,-1,-1,-1,
    # 2->2, 4->2, 6->4, 8->4, 10->6
    # 3 -> 3, 5 -> 3, 7->5, 9->5, 11->7, 13-> 7, 15-> 9, 17->9
    # if countPos > countNegatives:
    # equal case
 
    # # 1 1 -1 -1
    
    # if countPos == countNegatives and countNegatives & 1:
    #     return 1
    
 
    
    
    # if n&1:
    #     return countNegatives % 2
    # return countNegatives//2

   # Even Length
   # 1 -1 -1 -1  -> 1 operation -> 1 1 -1 -1
   # 1  1  1 -1  -> 1 operation
   # 1  1  1  1  -1 -> 1 operation
   # 1  1  1 -1 -1 -> 0 operation
    # if n & 1:
    #     return countNegatives
    # return countPos

    # if countPos>countNegatives:
        # 4 postivies, 3 negs then 1 operation
        # 4 - 3 is 1, ans is 1 
    # if countPos>=countNegatives:
    #    return 0

    # 1 1 1 -1 -1 -> 0
    # 1 1 1 1 -1 -1 -> 0
    # 1 1 1 1 -1 -> 1
    # 1 1 1 1 1 1 -1 -1 -1 -> 1

    # -1, -1, 1   -> 2 operation, n is even
    # -1,-1,-1, 1 -> 1 opertion, n is odd
    # -1,-1, -1, 1, 1 -> 1 operation, n is odd
    # -1,-1, -1,-1, 1 -> 2 operation, n is even
    # -1, -1, -1, -1, 1, 1 -> 2 operation

    # 1,-1 count is 0
    # 1 ,1, 1, - 1, -1, -1
    # 3,3

    # if countPos==0:
    #     return countNegatives
    # calc  = abs(countPos - countNegatives) 
    # if calc == 0 and countNegatives & 1:
    #    return 1
    # if calc < 2:
    #     return calc
    # return calc // 2
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    print(solve(n,array))