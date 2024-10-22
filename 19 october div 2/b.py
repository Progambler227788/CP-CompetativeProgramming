

def decimalToBinary(n,l): 
    return "{0:b}".format(int(n)).zfill(l)

for _ in range(int(input())):
    n = int(input())
    print(decimalToBinary( n - 1,n))