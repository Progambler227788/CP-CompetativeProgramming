def checking_is_it_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculateSmallestNumber():
    d = int(input()) 
    p1, p2 = 0,0 #prime 1 and prime 2
    # let say 1,x,y,a then I saw x*y is to be a for 4 divisors as x and y are primes
    i = d + 1
    while True:
        if checking_is_it_prime(i):
            p1 = i
            break
        i += 1

        # atleast d difference with previous prime factor that is p1
    
    i = p1 + d
    while True:
        if checking_is_it_prime(i):
            p2= i
            break
        i += 1
    
  # x *  y == a ,, 2 * 3 == 6, 3 * 5 == 15
    print(p1*p2)

t = int(input()) 
for _ in range(t):
    calculateSmallestNumber()

# focus on prime numbers because they don't have further divisors, if any number has further divisors so it could be smallest that would cause issues

