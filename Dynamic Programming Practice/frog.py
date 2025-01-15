def solve():
   n = int(input())
   array = list( map(int , input().split()  ))
   def minCost(array):
    n = len(array)
    if n == 2:  # Special case for just 2 stones
        return abs(array[1] - array[0])
    
    dp = [0] * n
    dp[0] = 0  
    dp[1] = abs(array[1] - array[0]) 
    
    for i in range(2, n):
        cost1 = dp[i - 1] + abs(array[i] - array[i - 1])
        cost2 = dp[i - 2] + abs(array[i] - array[i - 2])
        dp[i] = min(cost1, cost2)
    
    return dp[n - 1]
   
   print(minCost(array))   
solve()