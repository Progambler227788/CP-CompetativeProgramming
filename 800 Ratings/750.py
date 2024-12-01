n,k = map(int,input().split())
rem = 240 - k
if rem<5:
   print(0)
else:
   count = 1
   totalTime = 5
   while totalTime <= rem and count<=n:
          count+=1
          totalTime += count * 5
   print(count-1)
         
