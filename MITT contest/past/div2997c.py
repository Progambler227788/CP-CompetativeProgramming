def construct_sequences(test_cases):
    results = []
    for n in test_cases:
        # Generate a sequence with a periodic palindromic pattern
        pattern = list(range(1, (n // 2) + 2)) + list(range((n // 2), 0, -1))
        # Extend the pattern to fit the length n
        a = (pattern * ((n // len(pattern)) + 1))[:n]
        results.append(a)
    return results

# Example usage:
t = 3
test_cases = [6, 9, 15]
sequences = construct_sequences(test_cases)
for seq in sequences:
    print(*seq)

# 1 2 3 4 3 2 ,,, 