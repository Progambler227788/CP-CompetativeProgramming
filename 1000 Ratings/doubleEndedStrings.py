def tellCommonSubstring(a,b):
    m,n = len(a),len(b)
    dp=    dp = [[0] * (n + 1) for _ in range(m + 1)]
   
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
               dp[i][j] = 1 + dp[i-1][j-1]
            #    maxCount = max(maxCount,dp[i][j])
            else:
                dp[i][j] = 0
                
    maxCount = 0
                
    for i in range(1,m+1):
        for j in range(1,n+1):
               maxCount = max(maxCount,dp[i][j])
        
    print( (m+n) - (maxCount*2))
            

for _ in range(int(input())):
    a = input()
    b = input()
    tellCommonSubstring(a,b)