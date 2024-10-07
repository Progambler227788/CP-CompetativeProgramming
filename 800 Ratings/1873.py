def givePoints(i , j):
    # maping = {}
    # maping[0] = 1
    # maping[9] = 1

    # maping[1] = 2
    # maping[8] = 2

    # maping[2] = 3
    # maping[7] = 3
     
    # maping[4] = 5
    # maping[5] = 5
    # return maping[i]
    if i==0 or j==0 or i== 9 or j ==9:
       return 1
    if i==1 or j==1 or i== 8 or j == 8:
       return 2
    if i==2 or j==2 or i== 7 or j == 7:
       return 3
    if i==3 or j==3 or i== 6 or j == 6:
       return 4
    if i==4 or j==4 or i== 5 or j == 5:
       return 5
    
for _ in range(int(input())):
   counter = 0
   points = 0
   while counter<10:
      array = input()
    #   print(array)
      for index,value in enumerate(array):
          if value == 'X':
            points+= counter+1
            #  points+= givePoints(counter,index)
      counter+=1
   print(points)
    