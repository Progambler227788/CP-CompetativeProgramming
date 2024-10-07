import sys

sys.stdout = open('output.txt', 'w')  
sys.stdin = open('input.txt', 'r')

def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False  
    for i in range(2, limit + 1):
        if prime[i]:  
            for j in range(i * 2, limit + 1, i):  
                prime[j] = False
    
    return prime

def count_prime_subtractions(n, prime):
    ans = 0
    for i in range(2, n - 1):
        if prime[i] and prime[i + 2]:
            ans += 1
    
    # Add one more count if n >= 5, as there's a special case (5 is a prime)
    if n >= 5:
        ans += 1
    
    return ans

# Driver function
def main():
    N = 10**7 + 10  
    prime = sieve_of_eratosthenes(N) 
    tt = int(input()) 
    
    for qq in range(1, tt + 1):
        print(f"Case #{qq}: ", end="")
        n = int(input())  
        ans = count_prime_subtractions(n, prime) 
        print(ans)


main()
