# import sys
# sys.stdout = open('D:/CP/output.txt','w')
# sys.stdin = open('D:/CP/input.txt','r')
def giveMaximumNumber(sign,left,right,array):
    maximum = -10000000
    if sign == '+':
    
       
       for index,i in enumerate(array):
            if left <= i <= right:
               array[index] = i+1
           
            maximum = max(array[index] ,maximum)
    else:
       
       for index,i in enumerate(array):
            if left <= i <= right:
               array[index] = i-1
            maximum = max(array[index] ,maximum)
    return maximum
               
               
for _ in range( int(input())):
    n,operations = map(int, input().split())
    numbers = []
    data = list(map(int, input().split()))
    for _ in range(operations):
       sign,num1,num2 = input().split()
       numbers.append(giveMaximumNumber(sign,int(num1),int(num2),data))
    print(*numbers)
       
       