for _ in range(int(input())):
    n,l,r = map(int,input().split())
    arr = list(map(int,input().split()))
    diff = r-l
    bb = sorted(arr)
    print(sum(bb[:diff+1]))
    
    