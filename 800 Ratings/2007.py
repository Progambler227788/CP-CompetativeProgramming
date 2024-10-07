for _ in range(int(input())):
    l,r = map(int, input().split())
    countOdds = 0
    # two elements gcd is 2 if there are atleast two evens
    for i in range(l,r+1):
        if i&1:
            countOdds+=1
    print(countOdds//2)
