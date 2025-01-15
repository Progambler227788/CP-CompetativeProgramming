from collections import Counter

def min_operations_to_zero(t, test_cases):
    results = []
    
    for n, arr in test_cases:
        freq = Counter(arr)
        mex = 0
        operations = 0
        
        while freq:
            # Process elements for the current MEX
            while freq.get(mex, 0) > 0:
                freq[mex] -= 1
                if freq[mex] == 0:
                    del freq[mex]
                mex += 1
            
            # Increment operations and reset MEX
            operations += 1
            mex = 0
        
        results.append(operations)
    
    return results


# Input reading and processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Get results
results = min_operations_to_zero(t, test_cases)

# Output results
for res in results:
    print(res)
