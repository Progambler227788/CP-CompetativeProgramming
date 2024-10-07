import math

def max_good_array_length(l, r):
    return int((-1 + math.sqrt(1 + (2**3) *  ( r - l))) // 2) + 1
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(max_good_array_length(l, r))