# b = s/k
def tellArray(n, k, b, s ):
    if s<b*k or s>b*k + (k-1) * n:
       print(-1)
       return
    array = [0] * n
    s-= (b*k)
    array[0] = b * k
    for i in range( n ):
        temp = min(k-1,s)
        array[i]+= temp
        s-=temp
    print(*array)

    
t = int(input())
for i in range(t):
    n, k, b, s = map(int, input().split())
    tellArray(n, k, b, s )