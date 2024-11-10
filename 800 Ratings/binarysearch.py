def searchingArray(array,target,n):
    left = 0
    right = n-1
    mid = 0
    while left<=right:
        #   print(left)
        #   print(right)
          mid = (left+right) // 2
          if array[mid] == target:
            return True 
          elif array[mid] > target:
               right = mid - 1
          else:
              left = mid + 1
               
    return False
n,k = map(int,input().split())
array = list(map(int,input().split()))
searching = list(map(int,input().split()))
for target in searching:

    if searchingArray(array, target,n):
        print("YES")
    else:
        print("NO")
        

    