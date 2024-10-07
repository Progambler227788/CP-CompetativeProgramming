import math

def is_sum_of_consecutive(n):
    # Calculate the discriminant
    D = 1 + 8 * n
    
    sqrt_D = int(math.sqrt(D))
    if sqrt_D * sqrt_D != D:
        return False
    
    k = (-1 + sqrt_D) // 2
    
    return k > 0

# Test cases
for _ in range(int(input())):
    n = int(input())
    mango = "yes" if is_sum_of_consecutive(n) else "no"
    print(mango)
