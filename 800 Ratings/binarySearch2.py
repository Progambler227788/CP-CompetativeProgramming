# left closest

def searchingArray(array,target,n):
    left = -1
    right = n
    while left+1 < right:
          mid = ( left  +  right) // 2
          if array[mid] <= target:
              left = mid
          else: # if greater shrink to left
              right = mid
    return left+1 if left!=-1 else 0
n,k = map(int,input().split())
array = list(map(int,input().split()))
searching = list(map(int,input().split()))
for target in searching:
    print(searchingArray(array, target,n))
    