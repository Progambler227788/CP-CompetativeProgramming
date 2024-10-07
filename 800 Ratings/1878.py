# A. How Much Does Daytona Cost?

# subsegment can be of 1 length
for _ in range(int(input())):
    n,k = map(int, input().split())
    array = list( map(int, input().split()) )
    # it is simple as if element is in array then like 1 and segmenet is 1,3 so it has 
    if k in array:
        print("YES")
    else:
        print("NO")