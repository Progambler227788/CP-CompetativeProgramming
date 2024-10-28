def solve(array,n):
    totalSums = []
    for i in range(n):
        counts = 0
        temp = []
        maximum = max(array[0:i+1])
        totalMaxs = array[0:i+1].count(maximum)
        for j in range(i):
            if array[j]%2==0:
                if maximum==array[j] and totalMaxs>1:
                    totalMaxs-=1
                    counts += (array[j]//2)
                    temp.append(1)  
                elif  maximum==array[j] and totalMaxs<=1:
                      temp.append(array[j]) 
                else:
                    counts += (array[j]//2)
                    temp.append(1)          
            else:
                temp.append(array[j])  
             
        summing = sum(temp)
        summing-=maximum
        summing += maximum * (2**counts)
        totalSums.append(summing)
    print(*totalSums)

for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    solve(array,n)

