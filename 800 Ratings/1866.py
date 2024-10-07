def makeZeros(array):
    operations = float('inf')
    for i in array:
        operations = min( operations, abs(i))
    return operations

# for _ in range(int(input())):
n = int(input())
array = list(map(int,input().split()))
print(makeZeros(array))