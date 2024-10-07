def count_nines(num):
    return len(str(num)) - len(str(num).rstrip('9'))

def max_nine_pairs(n):
    max_nines = 0
    max_pairs = 0
    
    for i in range(1, n):
        sum_cost = 0
        for j in range(i, n + 1):
            sum_cost += j
            nines = count_nines(sum_cost)
            if nines > max_nines:
                max_nines = nines
                max_pairs = 1
            elif nines == max_nines:
                max_pairs += 1
    
    return max_pairs

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    print(max_nine_pairs(n))