def dna(n):
    A,C,G,T = 0,0,0,0
    e = len(n)
    left = 0
    while left < e:
            temp = 1
            currentChar = n[left]
            while left+1 < e and n[left+1] ==  currentChar : # AA
                  left+=1
                  temp+=1
            A = max(A,temp)
            
            left+=1 # move to next character

    return max(A,C,G,T)
n = input()

print(dna(n))