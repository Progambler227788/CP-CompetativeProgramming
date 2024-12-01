n = int(input())
array = list(map(int,input().split()))
countEvens,countOdds = 0,0
evenIndex,oddIndex = 0,0
for index,num in enumerate(array):
    if num & 1:
        countOdds+=1
        oddIndex = index + 1
      
    else:
        countEvens+=1
        evenIndex = index+1
print(evenIndex if countEvens==1 else oddIndex)
      