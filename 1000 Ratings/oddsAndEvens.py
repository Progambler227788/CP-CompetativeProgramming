def check(array,n):
    result = 'NO'
    if n&1:
        pass
    else:
        # even array
        oddIndexes = []
        evenIndexes = []
        totalSegments = 0
        i = 0
        
        while i < n:
            if array[i] & 1:
                oddIndexes.append(i)
            else:
                # pick only last even and go at end , like 2,4,6
                while i < n and array[i]%2==0:
                      i+=1
                if i==n-1:
                   return result
                evenIndexes.append(i)
        pick = 0
        for i in range(1, len(oddIndexes)):
            if oddIndexes[i-1]<evenIndexes[pick] and oddIndexes[i]>evenIndexes[pick]:
               
#
            
                
        