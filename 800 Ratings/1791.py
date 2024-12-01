def prepare(string,n):
    left , right = 0, n-1
    count = 0
    while left<=right:
          if string[left] == string[right]:
              count = (right - left + 1)
              break
            #   if left==right:
            #       count+=1
            #   else:
            #     count+=2
          left+=1
          right-=1
        #   else:
    print(count)
    
for _ in range(int(input())):
    n= int(input())
    s = input()
    prepare(s,n)
             
              
              
              