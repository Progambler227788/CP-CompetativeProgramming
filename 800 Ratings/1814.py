def solve(n,k):
    rem = n%2 # 3
    rem1 = n % k
    if rem1==0 or rem1%2==0 or rem==0 or rem%k==0 : # after dividing by k if rem is still divisble
       return "YES"
    # print(rem)
    # print(rem1)
    # if 2 + k == n:
    #    return "YES"
    return "NO"
for _ in range(int(input())):
   n,k = map(int, input().split())
   print(solve(n,k))

