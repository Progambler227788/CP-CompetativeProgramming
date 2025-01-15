for _ in range(int(input())):
    a = int(input())
    # a number is divisble by 33 if divisible by 3 and 11
    # a number is divisible by 33 direct check
    # either you remove consectives 33 or either you go for minise it by 33
    if a%33 == 0:
       print("YES")
    
    else:
         print("NO")
