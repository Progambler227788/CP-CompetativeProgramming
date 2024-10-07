import math

def count_coprime_triplets(l, r):
    # List to store the remaining numbers in the range [l, r]
    available_numbers = list(range(l, r + 2))
    operations = 0
    
    while len(available_numbers) >= 3:
        found_triplet = False
        
        for i in range(len(available_numbers) - 2):
            for j in range(i + 1, len(available_numbers) - 1):
                for k in range(j + 1, len(available_numbers)):
                    a, b, c = available_numbers[i], available_numbers[j], available_numbers[k]
                    if math.gcd(a, b) == math.gcd(b, c) == math.gcd(a, c) == 1:
                        # Remove this triplet from the list
                        available_numbers.pop(k)
                        available_numbers.pop(j)
                        available_numbers.pop(i)
                        operations += 1
                        found_triplet = True
                        break
                if found_triplet:
                    break
            if found_triplet:
                break
                
        if not found_triplet:
            break
    
    return operations

# Number of test cases
t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    result = count_coprime_triplets(l, r)
    print(result)
