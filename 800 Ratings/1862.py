# print([1] * 6)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    data = [arr[0]]
    # if n>=2:
    #     data.append(arr[1])
    # if arr[0] !=1:
      # 4 6 3 -> 4 1 6 1 3
    index = 1
    # duplicates = False
    # while index+1<n and arr[index+1] == arr[index]:
    #       data.append(arr[index])
    #       index+=1
    #       duplicates = True

    # if n>=2:
    #      if not duplicates and arr[0]>arr[1]:
    #         data.append(arr[1])
    #         data.append(arr[1])
    #      else:
           
    #         data.append(arr[1])
    # index = index + 1
          
          # 18 1 
          # 18 1 1
          # 18 17 17
    
    # if index<n and arr[index-1] == arr[index]:
    #    data.append(arr[index])
    #    index = 2
    while index < n:
        # if arr[index-1]> arr[index]:
        #    if arr[index] ==1:
        stored = arr[index]
       
        # duplicates = 0
        # while index+1 <n and arr[index+1] == stored:
        #       index+=1
        #       data.append(stored)
        #       duplicates +=1
        if arr[index-1] <=stored:
              data.append(stored)
        else:
            data.append(1)
            data.append(stored)
        index+=1
    print(len(data))
    print(*data)