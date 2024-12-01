string = input()
# countRight = len(string) - 1
# countLeft = 0
# # hello -> hel ,,,,,, lo
# findingleft = 'hel'
# findingRight = 'ol'
# cLeft = 0
# cRight = 0
# simulateL = findingleft[cLeft]
# simulateR = findingRight[cRight]

# while countLeft<countRight and (cLeft<3 or cRight<2):
#       if string[countLeft]==simulateL:
#           cLeft+=1
#       if string[countRight]==simulateR:
#           cRight+=1
#       countLeft+=1
#       countRight-=1
hello = "hello"
count= 0  
ans = "NO"
for i in string:
    if count>=5:
        ans = "YES"   
        break
    if i == hello[count]:
        count+=1
# jab loop break huga huskta count>=5 chaly hi na
if count>=5:
    ans = "YES"  
print(ans)
      # hello
          
      
# left for hel
# right for lo
