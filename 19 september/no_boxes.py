def factors(number):
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:  
                divisors.append(number // i)
    return sorted(divisors)

def makeBoxes(number,weights):
    k_s = factors(number)
    k_s = k_s[0: len(k_s) - 1]
    maxDiff = 0
    for k in k_s: # picking up k
        # issue was max or min ko age m 10**9 deta tu msla huga q k mne weights ko add krna ha 10**l , l can be large after adding
        # so isilye main focus is to inf always 
        maximum = float('-inf')
        minimum = float('inf')
        for index in range(0, len(weights), k):
            data = weights[index: index+k]
            picked = 0
            for i in data:
                picked+=i
            maximum = max(maximum,picked)
            minimum = min(minimum,picked)
        maxDiff = max(maxDiff, abs(maximum - minimum))
    return maxDiff
for _ in range(int(input())):
   number = int(input())
   weights = list(map(int, input().split() ) )
   print(makeBoxes(number, weights))


