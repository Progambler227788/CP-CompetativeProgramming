n = int(input())

MOD = 1000000007
def takeP(a,b):
    res = 1
    while b > 0 :
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b//=2 
    return res

print( takeP(2,n) )