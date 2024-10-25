import sys
import sys
sys.stdout = open('output1.txt','w')  
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
 
def solve():
    n, = map( int , input().strip().split() )
    a = list( map( int , input().strip().split() ) )
    l,r = 0,n-1
    while l < r:
        if 0 < l and a[l] != a[r]:
            # print(l,r)
            now = int(a[l] == a[l-1]) + int(a[r] == a[r+1])
            change = int(a[r] == a[l-1]) + int(a[l] == a[r+1])
            if change < now:
                a[l],a[r] = a[r],a[l]
        l += 1
        r -= 1
    out = 0
    for i in range(1,n):
        out += int(a[i] == a[i-1])
    print(out)
 
 
 
 
 
 
for i in range(int(input().strip())):
    solve()