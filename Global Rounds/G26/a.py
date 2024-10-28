def solve():
    n,m,r,c = map( int, input().split() )

    remRows = n - r
    totalUps = remRows * m # total columns 
    # print(remRows)
    totalLefts = (m-c) + (remRows * (m-1) )
    # print((m-c))
    # upr le kr jany k cost total columns k barabar ari ha
    # left ko move krny k cost 1 ha
    print(totalUps + totalLefts)
for _ in range(int(input())):
    solve()