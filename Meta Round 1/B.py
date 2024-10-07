import math

def give_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [p for p in range(2, n + 1) if sieve[p]]

primes = give_primes(200)
primes = sorted(primes)

def solve(n):

    # primes = give_primes(n)
    # print(primes)
    prime_set = set(primes) 
    setting = set()
    for j in range(len(prime_set)):
        if primes[j] > n:
            break
        for i in range(j):
            if primes[i] <n and primes[j] - primes[i] in prime_set:
               setting.add(primes[j] - primes[i])

    return len(setting)

maping = {}
for ele in primes:
    maping[ele] = solve( ele )
    print(ele,maping[ele])

# for _ in range(int(input())):
#     n = int(input())
#     print(solve(n))

# # Test with n = 10^6
# n = 8
# result = count_n_subtractorizations(n)
# print(f"Count of {n}-subtractorizations: {len(result)}")
