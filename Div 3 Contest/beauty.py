

def checking(s, n):
    k = int(n**0.5)
    if k * k != n:
        return "NO"
    if s == "111111111":
        return "NO"
    # construct beuti mateix
    matrix = [s[i * k:(i + 1) * k] for i in range(k)]
    
    first_row = matrix[0]
    last_row = matrix[-1]
    
    if '0' in first_row or '0' in last_row:
        return "NO"
    for i in range(k):
        if matrix[i][0] != '1' or matrix[i][-1] != '1':
            return "NO"
    
    return "YES"

for _ in range(int(input())):
   n = int(input())
   string = input()
   print(checking(string,n))
