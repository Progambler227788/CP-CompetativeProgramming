# def takePower(a,b):
#     # if b & 1: # odd
#     #    return a * (a**2)**(  (b-1 ) // 2) %  (1000000000 + 7)
#     # return  ( (a**2)**( b // 2)  )   %  (1000000000 + 7)
#     if b==0:
#        return 1
#     return  ( a**b )  % (  (10**9) + 7 )

MOD = 1000000007
def takePower(a, b):
    if b == 0:
       return 1 
    if b == 1:
       return a % MOD
    calc = takePower(a, b//2 )
    if b%2==0: # b & 1
       return  (calc*calc) % MOD

    return (((calc*calc) % MOD ) *a)  % MOD  

def takeP(a,b):
    res = 1
    while b > 0 :
        if b %2!=0:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b//=2 # b//=2
    return res


for _ in range(int(input())) :
    a,b = map(int, input().split())
    print(takeP(a,b))