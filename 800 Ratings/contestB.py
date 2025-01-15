def convert(list):
    
    s = [str(i) for i in list]
    
    res = int("".join(s))
     
    return(res)
def solve(s):
    total = 0 
    array = []
    for i in s:
        array.append(int(i))
        total += int(i)
    if total%9==0:
        print("YES")
        return
    for i, ele in enumerate(s):
        m = int(ele)
        sq =  m  * m
        for j in range(i+1, len(s)):
            
            took = int(s[j]) 
            sq1 = took * took
            if sq1<10 and sq<10:
               array[i] = sq
               array[j] = sq1
               nn = convert(array)
               tt = nn % 9
               if tt == 0:
                   print("YES")
                   return
               
            if sq1>10 and sq<10:
               array[i] = sq
               array[j] = took
               nn = convert(array)
               if nn%9 == 0:
                   print("YES")
                   return
               
            if sq1<10 and sq>10:
               array[j] = sq1
               array[i] = m
               
               nn = convert(array)
               if nn%9 == 0:
                   print("YES")
                   return
               
            
    print("NO")
    

for _ in range(int(input())):
    s = input()
    solve(s)
    