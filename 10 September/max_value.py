from itertools import combinations
from functools import lru_cache
class Solution:
 def maxValue(self, nums, k: int) -> int:
    n = len(nums)
    if n < 2 * k:
           return 0
    max_xor = float('-inf')

    @lru_cache(None)
    def dp(i, count):
            if count == 2 * k:
                return float('-inf')
            if i >= n:
                return 0
            # Option 1: Skip current element
            max_xor = dp(i + 1, count)
            
            # Option 2: Include current element
            max_xor = max(max_xor, dp(i + 1, count + 1))
            
            return max_xor
    def compute_or(subset):
        result = 0
        for num in subset:
                result |= num
        return result
    for indices in combinations(range(n), 2 * k):
        subsequence = [nums[i] for i in indices]
        
        f1 = subsequence[:k]
        f2 = subsequence[k:]
        

        max_xor = max(max_xor,  compute_or(f1) ^  compute_or(f2))
    
    return max_xor
        