def solve(n,k):
    rem = n%2 # 3
    rem1 = n % k
    check = n - k
    # 2*x + y*k = n
    # at first attempt i was not ev
    # basic maths -> either divided by 2 or k, or either n - k will be divide by 2 as k would be greater than 2
    if rem1==0 or rem==0 or check%2==0: # after dividing by k if rem is still divisble
       return "YES"
    return "NO"
for _ in range(int(input())):
   n,k = map(int, input().split())
   print(solve(n,k))

