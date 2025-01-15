def solve():
    d = [int(y) for y in list(input())]
    two = d.count(2)
    three = d.count(3)
    s = sum(d)
    if s%9==0:
         print("YES")
         return
    f1 = min(7,two)
    f2 = min(7,three)
    
    for x in range(f1+1):
        for y in range(f2+1):
            if (s+ 2*x + 6*y) % 9 == 0:
               print("YES")
               return     
    print("NO")

for _ in range(int(input())):
    solve()

