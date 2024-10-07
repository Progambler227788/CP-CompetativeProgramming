 
# sum of numbers to remaining elements, think of maximum

def goodPrefix(size,numbers):
    count = 0
    prefixSum = 0
    maximum = numbers[0]
    for right in range(size):
        # print(right)
        prefixSum += numbers[right]
        maximum = max(numbers[right],maximum)
        if maximum  == prefixSum - maximum:
               count+=1
    print(count)
    
for _ in range( int(input())  ):
    size = int(input())
    data = list(map(int, input().split()))
    goodPrefix(size,data )