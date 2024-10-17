n,k = map(int, input().split())
array = list(map(int, input().split()))
temp = k
# count = k
if k == n and array[k-1]!=0:
    print(k)

elif array[temp-1] == 0:
     count = 0
     for i in array:
          if i>0:
               count+=1
     print(count)
else:
    while k<n and array[k] == array[temp-1]:
      k+=1
    print(k)

# elif array[temp] == 0 and temp==k:
#     print(0)
# else:
    


