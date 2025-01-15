def giveTotalShops(arr,n,k):
    l,r = 0,n
    while l<r:
          mid = l + (r-l) // 2
          if arr[mid]<=k:
              l = mid + 1
          else:
              r = mid 
    return l

shops = int(input())
shopsData = list(map (int, input().split()))
coins = []
totalDays =int(input())
output = []
shopsData = sorted(shopsData)
for _ in range( totalDays):

    c = int(input())
    output.append( giveTotalShops(shopsData,shops,c))
    
    # print the output
for i in output:
    print(i)
    
