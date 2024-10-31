def solve(array,k):
    given = 0
    current = 0
    for gold in array:
        # will take all gold
        if gold>=k:
            current += gold
        elif gold == 0 and current>0:
            current-=1
            given+=1
    print(given)

for _ in range(int(input())):
    n,k = map(int,input().split())
    data = list(map(int,input().split()))
    solve(data,k)
        
             