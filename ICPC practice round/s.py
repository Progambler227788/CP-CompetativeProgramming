def max_money_spent(test_cases):
    results = []

    def dfs(garments, budget, current_garment, memo):
        if budget < 0:
            return -float('inf') 
        if current_garment == len(garments):
            return 0  

        if (current_garment, budget) in memo:
            return memo[(current_garment, budget)]

        max_spent = -1
        for price in garments[current_garment]:
            spend = dfs(garments, budget - price, current_garment + 1, memo)
            if spend != -float('inf'):  
                max_spent = max(max_spent, spend + price)

        memo[(current_garment, budget)] = max_spent
        return max_spent

    for budget, num_garments, garments in test_cases:
        memo = {}
        result = dfs(garments, budget, 0, memo)
        results.append(result if result != -float('inf') else -1)

    return results

num_test_cases = int(input())
test_cases = []

for _ in range(num_test_cases):
    budget, num_garments = map(int, input().split())
    garments = []
    
    for _ in range(num_garments):
        num_models = int(input())  
        prices = list(map(int, input().split()))
        garments.append(prices)
    
    test_cases.append((budget, num_garments, garments))

output = max_money_spent(test_cases)
for res in output:
    print(res)
