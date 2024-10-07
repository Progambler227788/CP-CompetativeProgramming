
for _ in range(int(input())):
    arrays = int(input())
    minimum = 10**10
    minimum_2nd = 10**10
    totalSum = 0
    for i in range(arrays):
        size = int(input())
        store = sorted( map(int,input().split()))
        minimum = min( minimum, store[0]) # first minimum
        minimum_2nd = min( minimum_2nd, store[1]) # 2nd minimum
        totalSum += store[1] # add up all second minimum elements
    print( minimum+totalSum-minimum_2nd)

