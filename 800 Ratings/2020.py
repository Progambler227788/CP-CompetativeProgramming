def solve(n,k):
  if n < k or k==1:
     return n
  count = 0

  # 5 2, 5%2 is 1, 2%2
  while n>0:
        count+=n%k 
        # print(n%k)
        n = n//k
        
  return count


for _ in range(int(input())):
  n,k = map(int, input().split())
  print(solve(n,k))
  