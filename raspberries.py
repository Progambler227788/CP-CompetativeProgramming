
# import sys
# sys.stdout = open('D:/CP/output.txt','w')
# sys.stdin = open('D:/CP/input.txt','r')
def operationsNeed(numbers,k):
    maxMod = -10000
    evenCount = 0
    divisible = False
    for num in numbers:
        num%=k
        if num: # remainder greater than 0
            maxMod = max(maxMod,num) # num has remainder now
        else:
           divisible = True # one divisor found
        if num == 2: # even numbers counting
            evenCount+=1
    if divisible:
        return 0
    elif k == 4:
        if evenCount>=2:
            return 0 
        elif evenCount>=1 or maxMod == 3: # 3,7 so only one opertion or either only one even nunber
            return 1
        
        return 2

        # operations case as largest mod is closest number
        # for example in case of 3,7. 2%3 is 2 and 7%3 is 1 so 2 is chosen and 3-2 == 1
        # In case of 2, it will be either 0 or 1 so accordingly we have to follow.
        # In case of 3, it will be either 0,1,2
        # In case of 4, it will be either 0,1,2,3 (Non Prime Number)
    return  k - maxMod
        
         
           


           
            
               
for _ in range( int(input())  ):
    size,k = map(int, input().split())
    data = list(map(int, input().split()))
    print(operationsNeed(data,k ))