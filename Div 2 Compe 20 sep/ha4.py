import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')
# def giveSmallerValue(energy,maping):
#     # print(f'Energy clalled {energy}')
#     result = -1
#     # print(finding)
#     for key,value in sorted(maping.items(),key =lambda x : x[1]):  # Sort keys to check in order
#       if value < energy:
#          result = key
#          break  
#     return result


def giveSmallerValue(energy,maping):
    result = -1
    thatValue = float('inf')
    # sorted(maping.items(),key =lambda x : x[1])
    for key,value in enumerate(maping):  # Sort keys to check in order
      if value < energy and value < thatValue:
         result = key
         thatValue= value
    return result

def get_key_by_value(maping, value):
    return maping.index(value)

def solveIt(n,goal,energies):
    maping = [float('inf')] * (n+1)
    print(maping)

    for index,value in enumerate(energies):
        # print(maping)
        smaller = giveSmallerValue(value,maping)
        # print(f'smaller : {smaller}')
        if smaller !=-1:
           smallerStone = maping[smaller]
           remaining = value - smallerStone
           currentEnergy = smallerStone
           print(remaining)
        #    previousEnergy = smallerStone

           while remaining>0:
                currentEnergy+=1
                if currentEnergy in maping:
                   key = get_key_by_value(maping,currentEnergy)
                   previousEnergy = currentEnergy
                   maping[smaller] = currentEnergy 
                   smaller = key
                # print(remaining)
                # print(maping)
                remaining-=1
        #    print(maping)
           maping[index+1] = smallerStone   # us key pa ab new element agaye ga jiski energy zada
           maping[smaller] = currentEnergy
      
        else:  
            maping[index+1] = value
    print(maping)
    equalIndex = n
    equalDiff = float('inf')
    for key,position in enumerate(maping):
        temp = abs(position - goal)
        if temp == equalDiff:
           if key < equalIndex:
              equalIndex = key
           equalDiff = temp
        elif temp < equalDiff:
            equalIndex = key
            equalDiff = temp

    return equalIndex,equalDiff
          
           



              
           
# 7 8, 9
#
           



for t in range(int(input())):
    n, goal= map(int, input().split())
    energies = []
    for i in range(n):
        energies.append( int(input()) )
    a,b =solveIt(n,goal,energies)
    print(f"Case #{t+1}: {a} {b}")
    # solveIt(n,goal,energies)