def missingNumber( n, array):
    takeSum = n * (n+1) //2
    for i in array:
          takeSum = takeSum - i

    return takeSum
n = int(input())
array = list(map(int, input().split()))
print(missingNumber(n,array))