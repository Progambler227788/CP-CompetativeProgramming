# import sys
# sys.stdout = open('output.txt','w')  
# sys.stdin = open('input.txt','r')
def get_all_substrings_generator(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]

def promise(string,size):
    
    # for counting equals
    p,n = 0,0
    for i in string:
        if i =='+':
         p+=1
        else:
          n+=1
    if p==n:
       return True
    else:
    
       count = 0
       i = 0
       pairs = 0

       while i < size:
          if string[i] == '-':
             pairs+=1
          else:
             count +=  (pairs//2)
             pairs = 0
             singles = n - (count * 2)
             if p+count == (singles):
                  return True
          i+=1
       count +=  (pairs//2)
       singles = n - (count * 2)


       if p+count == (singles):
          return True
    return False


              

for _ in range(int(input())):
    n = int(input())
    data = input()
    dp = {}
    ans = 0
    for i in range(n):
      p,neg = 0,0
      count = 0
      pairs = 0
      singles = 0
      for j in range(i,n):
          if data[j] == '+':
             p+=1
          else:
            neg+=1
      if p == neg :
         ans+=1
         continue
      else:
        
        for j in range(i,n):
            if data[j] == '-':
               pairs+=1
            else:
               count +=  (pairs//2)
               pairs = 0
               singles = neg - (count * 2)
               if p+count == (singles):
                    ans+=1
                    continue
        count +=  (pairs//2)
        singles = neg - (count * 2)           
        if p+count == (singles):
            ans+=1
    
    print(ans)
    