for _ in range( int(input())):
    n,m = map(int, input().split())
    d = list(map(int, input().split()))
    p = int(input())
    boolean = True
    for i in range(n-1):
        if d[i] > d[i+1]:
            boolean = False
            break
    output = "YES"
    if not boolean:
       big , bigI = 0,0
       d[0] = min( d[0], p-d[0] )
       for index in range( 1, n):
           diff =  p - d[index]
           if min(d[index],diff) >= d[index-1]:
                 d[index] = min(d[index],diff)
           elif max(d[index],diff) >=d[index-1]:
                 d[index] = max(d[index],diff)
           else:
                 output = "NO"
                 break
    print(output)
        