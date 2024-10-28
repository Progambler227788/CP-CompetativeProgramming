def solve(n):
    if n==1 or n ==3:
        return -1
    yes = True if n & 1 else False
    string = ''
    if yes:
      string = '3'*(n-5) + '36366'
    else:
       string = '3'*(n-2) + '66'
    return string

for _ in range(int(input())):
   print(solve(int(input())))

      
    
    

    
