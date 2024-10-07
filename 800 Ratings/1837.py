def solve(target,k):
    if target < k or target%k!=0:
       print(1)
       print(target)
       return
    print(2)
    print(target-1,1) # 4 2 


for _ in range(int(input())):

    target,k = map(int, input().split())
    solve(target,k)
