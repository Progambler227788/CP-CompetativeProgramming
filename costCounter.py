

def giveCost(elements,costs,k,size):
    #aagr tu mra k costs k minimum se hi chota h tu m ko use kruga n times that's it
    
    # agr mra k bra ya brabar a tu sab se phly min of costs waly ko dedo ga
    # Combine the lists into a list of pairs (,) tuples
 
    # [1,3,4] [2,4,4] -> (1,2) , (3,4) , (4,4)
    combined = list(zip(elements, costs))
    # Sort the combined list based on the second element of each tuple (costs values)
    # x[1] mean second element second elemnt that is cost
    sorted_combined = sorted(combined, key=lambda x: x[1])
    # Unzip the sorted list back into two separate tuples
    sorted_ai, sorted_bi = zip(*sorted_combined)

    elements = list(sorted_ai)
    costs = list(sorted_bi)

    if k <= costs[0]:
       return k*size # let say k is 2 and elements were 3 then 2*3 will work as 6 costs
    
    if size == 1:
       return k
   
 # 1 is for minimum because usko tu phly hi mili gi or usky bd usny ktno ko di wo usky upr ata ha
    # depend on minum elemnents whom he already transferred, he will transfer to next ai elements
    totalCost = k
    totalElementsDone = 1
       

    if totalElementsDone == size: # our minimum did things for us then no cost need more
       return totalCost
    # print(totalElementsDone)
    
    left = 0
    right = size- 1
    
    while left<=right:
        #   print(costs[left])
          remaining = size - totalElementsDone
          if remaining <= 0:
           break
        #   print(remaining)
          if costs[left] <k:
            if elements[left] >= remaining:
                totalCost +=  (costs[left] * remaining) 
                totalElementsDone += remaining
         
            else: # in case he can't pass to every one
                totalCost += (costs[left] * elements[left]) 
                totalElementsDone += elements[left]
          else: # as I did break here so it added wrong
              totalCost += k * remaining
              totalElementsDone = size
              return totalCost
          left+=1
    
    return totalCost
             
            

for _ in range(int(input())):
   n,k = map(int, input().split())
   A = list(map(int, input().split()))
   Costs =  list(map(int, input().split()))
   print(giveCost(A,Costs,k,n ))
