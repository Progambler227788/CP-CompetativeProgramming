def solving(n,p):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for lengthing in range(2, n + 1):  
            for i in range(1, n - lengthing + 2): 
                j = i + lengthing - 1  
                dp[i][j] = float('inf') 
                for k in range(i, j): 
                    cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    dp[i][j] = min(dp[i][j], cost)
        print(dp[1][n])


for _ in range( int(input()) ):
        n = int(input())  
        p = list(map(int, input().split())) 
        solving(n,p)
    