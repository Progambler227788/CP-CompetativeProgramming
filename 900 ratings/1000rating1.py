import math
n,m,a = map(int  , input().split())

# total length
tL = math.ceil(n/a)

# total width
tW = math.ceil(m/a)

print(tL * tW)