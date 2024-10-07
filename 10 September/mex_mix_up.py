def computeXOR(n) : 
    # Modulus operator are expensive  
    # on most of the computers. n & 3  
    # will be equivalent to n % 4. 
  
    if n % 4 == 0 : 
        return n 
 
    if n % 4 == 1 : 
        return 1

    if n % 4 == 2 : 
        return n + 1
    
    # If n%4 gives remainder 3 
    return 0

def giveLength(mex,xor):
    prev = computeXOR(mex-1)
    if prev == xor:
       return mex 
    choose = prev ^ xor
    if choose == mex:
       # Like if there is 1 that does not need to be include so what we can do? we can take two numbers equivalent to 1 2020^2021 == 1^1 == 1
       return mex + 2 # two more elements as they will form same xor for given element
    else:
      return mex+1 
    
for _ in range(int(input())):
    a,b = map(int, input().split())
    print(giveLength(a,b))

