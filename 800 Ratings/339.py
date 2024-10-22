# 
from collections import defaultdict
def solve():
    array = input()
    picked = defaultdict(str)
    countOnes = 0
    countTwos = 0
    countThrees = 0
    countPlus = 0
    for value in array:
        if value == '1':
           countOnes+=1
        elif value =='2':
           countTwos+=1
        elif value == '3':
           countThrees+=1
        else:
           countPlus+=1

    string = ""
    while countOnes!=0:
        string+='1'
        countOnes-=1
        if countPlus>0:
          string+='+'
          countPlus-=1
    while countTwos!=0:
        string+='2'
        countTwos-=1
        if countPlus>0:
          string+='+'
          countPlus-=1
    while countThrees!=0:
        string+='3'
        countThrees-=1
        if countPlus>0:
          string+='+'
          countPlus-=1
    print(string)
solve()

    
        
      

# 1+2+3