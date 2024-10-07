
def takeSum(start,end):
    data = 0
    while start<=end:
        data+= (-start)
        start+=1
    return data
         
         
def a1(n,k):
    minimum = 10**9
    if n==2:
        print(1)
        return
    ending = k+n-1
    i  =  k +1
    left = 0
    right = takeSum(i,ending)
    for i in range(k + 1, ending):
        # Update left sum incrementally
        left += i - 1
        # Update right sum incrementally
        right = right + i
        # Calculate the minimum
        minimum = min(minimum, abs(left + i + right))
        if minimum == 0:
            break
    print(left)
    print(right)
    print(minimum)

for _ in range(int(input())):
    n,k= map(int, input().split())
    a1(n,k)

    
