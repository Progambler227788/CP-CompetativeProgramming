
def checkOptimal(  array, n, target):
    #   petrol = choosen
    #   withInRange = False
      diff = float('-inf')
      prev = 0
      for i in range( n):
        diff = max(    diff,  array[i] - prev )
        prev = array[i]
        # if array[i] - array[i-1 ] > choosen:
        #    return False
    #   if 2 * (target - array[-1]) >= choosen:
    #      return False
      return max( diff,  2 * (target - array[-1])      )
      
        
      
           
def travel(n,array,x):
    # if n == 1:
    #     return array[0]

    return checkOptimal( array, n, x)
        
          
           
    # while count<x and targetPetrol>0:
    #       if choosen in array:
    #         targetPetrol = choosen # refill
    #       count+=1
    #       targetPetrol-=1
    #     #   print(targetPetrol)
          
    #       if count == x:
    #          return choosen
    #       if count!=x and targetPetrol<=0:
    #          choosen+=1
    #          targetPetrol = choosen
    #          count = 0
          
    # return choosen
          
    

    # for repeat in range(n):
    #   for i in range(1,n):
    #     array[i:i+k] = sorted(array[i:i+k])
    #     array[i-1:i+k-1] = sorted(array[i-1:i+k-1])
    # for i in range(1,len(array)):
    #     if array[i-1]> array[i]:
    #        return "NO"
    # return "YES"


for _ in range(int(input())):
    n,k = map(int, input().split())
    array = list( map(int, input().split()) )
    print(travel(n,array,k))


    # 2 3 1
    # 2 3 1
    # 2 3 1
    # 2 1 3