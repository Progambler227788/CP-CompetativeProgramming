import sys
sys.stdout = open('output.txt','w')  
sys.stdin =  open('input.txt','r')

def find_combinations(goal):
    # Dictionary to store the result for each product `target_product`
    product_map = {}
    
    # List to hold the current combination of factors
    current_combination = []

    # Recursive DFS function to explore all combinations
    def dfs(current_sum, current_product, start_factor):
        if current_sum == goal:
            # If we reach the goal, store the combination if it's new or smaller
            if current_product not in product_map or len(current_combination) < len(product_map[current_product]):
                product_map[current_product] = list(current_combination)
            return
        
        # Try all possible values starting from `start_factor`
        for factor in range(start_factor, goal - current_sum + 1):
            current_combination.append(factor)
            dfs(current_sum + factor, current_product * factor, factor) 
            current_combination.pop()

    dfs(0, 1, 1)

    return product_map

# Input processing and output
def main():
    goal = 41
    product_map = find_combinations(goal)  # Precompute all possible products up to the goal
    
    t = int(input())  # Number of test cases
    for test_case_num in range(1, t + 1):
        print(f"Case #{test_case_num}:", end=" ")
        target_product = int(input())
        if target_product not in product_map:
            print(-1)
        else:
            result = product_map[target_product]
            print(len(result), *result) 

if __name__ == "__main__":
    main()
