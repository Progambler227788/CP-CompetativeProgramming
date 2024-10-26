
def solve(array,n):
    current = n
    i = current - 1
    while i>=0:
        # print(array[i],current)
        print(i)
        if i ==  (abs(current) - array[i]):
            current =  current + (i) # increment size
            array.extend( [0] * (i))
            i = current - 1
        else:
           i-=1
    print(current)

for _ in range(int(input())):
    n = int(input())
    array =list( map(int, input().split()))
    solve(array,n)

    