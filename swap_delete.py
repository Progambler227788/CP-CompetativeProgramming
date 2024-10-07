
def getOperations(s):
    countZeros = 0
    countOnes = 0
    for i in s:
        if i == '0':
           countZeros+=1
        else:
            countOnes+=1
    t = ''
    i = 0
    while countZeros>0 or countOnes>0:
        if s[i] == '0':
           if countOnes == 0:
              break
           t+='1'
           countOnes-=1
        else:
           if countZeros == 0:
              break
           t+='0'
           countZeros-=1
        i+=1
    # print operations
    print( abs(len(s)) - abs(len(t)))
          
      

testCases = int(input())

for t in  range(testCases):
     # Read number of students
    s = input()
    getOperations(s)

    
    
