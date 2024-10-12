def solve():
    n,k,x = map(int,input().split())
       
    if x!=1:
       print("YES")
       print(n)
       arr = [1] * n
       print(*arr)
    
    else:
      # x is 2,
      if k==1:
         print("NO")
      elif n%2==0:
         
         print("YES")
         c = n//2
         print(c)
         arr = [2]*c
         print(*arr)
      else:
   
         half = n//2
         if k>=3:
         # equation = k-1 * 2 + 3
         # 11 -> 5*2 + 1
         # 11 -> 2*4 + 3
         # if equation!=n:
         #    print("NO")
         #    return
           print("YES")
           arr = [2] * (half-1)
           arr.append(3)
           print(half)
           print(*arr)
         else:
            print("NO")
         
    
for _ in range(int(input())):
   solve()