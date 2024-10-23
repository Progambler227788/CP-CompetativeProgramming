def solve(array,n):
    m = array[0]
    p = array[-1]
    if m == p:
        print("NO")
    else:
        print("YES")
        print(p, end= ' ')
        print(*array[0:n-1])
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    solve(array,n)