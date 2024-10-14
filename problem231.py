def solve():
    count = 0
    for _ in range(int(input())):
        x,y,z = map(int,input().split())
        if (x==1 and y==1) or (x==1 and z==1) or (y==1 and z==1):
           count+=1
        
    print(count)

        
    
solve()
    