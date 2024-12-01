for _ in range(int(input())):
    # in case of less than wrong make number 1 = number 2 -1
    s = input()
    n1,op,n2 = int(s[0]) , s[1] , int(s[2])
    data = ''
    if op == '<':
        # 9 < 8
       op = '<'
       if not n1 < n2:
          if n1==n2:
               op = '='
          else:
             op = '>'
       data = str(n1) + op + s[2:]
    
        
    elif op == '>':
       if not n1 > n2:
           if n1==n2:
               op = '='
           else:
             op = '<'
      
       data = str(n1) + op + s[2:]
        
    else:
        if not n1==n2:
            n1 = n2
        data = str(n1) + s[1:]
    print(data)
        
           
       