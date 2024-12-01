# right closest

def searchingArray(array,target,n):
    left = -1
    right = n
    while left +1 < right:
          mid = ( left  +  right) // 2
          # no need to look at left side as we are finding element greater than target
          if array[mid] < target:
              left = mid
          else:
              right = mid
    return right+1 if right!=n else n+1
n,k = map(int,input().split())
array = list(map(int,input().split()))
searching = list(map(int,input().split()))
for target in searching:
    print(searchingArray(array, target,n))
    