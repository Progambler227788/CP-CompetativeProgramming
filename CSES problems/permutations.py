from itertools import permutations




def solve():
  n = int(input())
  
  if n==1:
     print(1)
     return
  if n==2 or n==3:
     print("NO SOLUTION")
     return
  stored = []
  for i in range(2,n+1,2):
      stored.append(i)
  for i in range(1,n+1,2):
      stored.append(i)
  print(*stored)


# 1 2 3 4 5

# Permutations m yad rkho aik even,odd pair, aik reverse krky pair
solve()

# A permutation of integers 1,2 … N is called beautiful if there are no adjacent elements whose difference is 1. 
# Given N,
# construct a beautiful permutation if such a permutation exists. If there are no solutions, print “NO SOLUTION”.
