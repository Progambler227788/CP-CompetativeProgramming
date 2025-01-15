
for _ in range(int(input())):
    n , m = map(int,input().split())
    totalWords = 0
    
    for i in range(n):
        s = input()
        m-= len(s)
        if m>=0:
            totalWords += 1
            
       
      
    print(totalWords)
  