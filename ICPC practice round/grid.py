def max_charge(n,m,grid):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # start maru
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
          
            elif i == 0:
                # phli row m upr se ni askty pichly column se ajo
                dp[i][j] = dp[i][j - 1] + grid[i][j]
         
            elif j == 0: # phly column m b same upr wlai logic right se ni aty
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:# baki sab ko nikali jao 
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[n - 1][m - 1]

for _ in range(int(input())):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        print(max_charge(n,m,grid))
