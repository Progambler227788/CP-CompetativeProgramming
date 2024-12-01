for _ in range(int(input())):
    n,a,b = map(int , input().split())
    if a>=b:
        print(a*n)
    else:
        covered = b - a 
        tt = min(n,covered)
        left = ((b + (b-tt+1)) * (tt)) //2
        # print(left)
        total = left + (n - tt) * a
        
        print(total)
              
#     7
# 4 4 5
# 5 5 9
# 10 10 5
# 5 5 11
# 1000000000 1000000000 1000000000
# 1000000000 1000000000 1
# 1000 1 1000
