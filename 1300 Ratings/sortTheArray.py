def solve(array,n):
    compare = sorted(array)
    # sab se bra and then so on less
    left = -1
    right = -1
    for i in range(1,n):
        if array[i-1]>array[i]:
           left = i-1
           break
    for i in range(1,n):
        if array[i-1]>array[i]:
           right = i
    
    # already sorted
    if left ==-1 and right==-1:
        print("yes")
        print("1 1")
    else:
        array[left:right+1] = reversed(array[left:right+1] )
        for i in range(n):
            if compare[i] != array[i]:
               print("no")
               return
        print("yes")
        print(str(left+1)+' '+str(right+1))
               
n = int(input())
solve(list(map(int,input().split())),n)


    

              
             