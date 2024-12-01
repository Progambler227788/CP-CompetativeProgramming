def count_valid_y(x, m):
    valid_y_count = 0
    
    # Iterate over y from 1 to m
    for y in range(1, m + 1):
        if y == x:  # We want y != x
            continue
        
        xor_value = x ^ y  # Calculate x ⊕ y
        
        # Check if the XOR result is a divisor of x or y
        if (x % xor_value == 0) or (y % xor_value == 0):
            valid_y_count += 1
    
    return valid_y_count

# Input processing
t = int(input())  # number of test cases
for _ in range(t):
    x, m = map(int, input().split())
    result = count_valid_y(x, m)
    print(result if result > 0 else 0)
