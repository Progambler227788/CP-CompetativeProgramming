def giveTotal(n,k):
    count = 0
    for i in range(1,n):
        for j in range(i+1,n+1):
            if (i+j) % k == 0:
                count+=1
    return count

for _ in range(int(input())):
    N,K = map(int,input().split())
    print(giveTotal(N,K))