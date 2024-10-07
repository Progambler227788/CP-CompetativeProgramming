
#3,4,5,6,8
from collections import defaultdict

def maxMod(a):
    maxi = 0
    if a>=3:
       maxi = max(maxi, a // 3, a//4, a//5, a//6, a//8) # 4/3 -> 1
    # if a>=4:
    #    maxi = max(maxi, a % 3, a%4, a%5, a%6, a%8)
    # if a>=5:
    #    maxi = max(maxi, a % 3, a%4, a%5, a%6, a%8)
    # if 
       
    return maxi
def solve(sticks):
    maping = defaultdict(int)
    for i in sticks:
        maping[i]+=1
    counts = 0
    for _,value in maping.items():
        counts += maxMod(value)
    return counts

for _ in range(int(input())):
    n = int(input())
    sticks = list(map(int, input().split()))
    print(solve(sticks))