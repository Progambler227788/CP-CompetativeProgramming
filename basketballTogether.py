# bara huny m ktna time laga us hisab se

''' 50 60 70 80 90 100

100 50 -> 100+100
60 70 90 -> 90 90 90

100

100,100
90,90
80,80
optimal got 3 wins

100

60,60
80,80
100,100'''

# 100 50

def giveWins(d,array):
    dataSorted = sorted(array,reverse=True)
    countWins = 0
    left = 0
    right = len(dataSorted) - 1

    while left <= right: # iterate over each sorted list
        if dataSorted[left] > d:
           countWins+=1 # 1 team won
        else:
           count = dataSorted[left]
           while  left<right and count<=d:
                right-=1
                count  += dataSorted[left]
        #    print(count)
           if count>d:
              countWins+=1
        left+=1
    print(countWins)


candidates, d = map(int, input().split())
array = list(map(int, input().split()))
giveWins(d,array)