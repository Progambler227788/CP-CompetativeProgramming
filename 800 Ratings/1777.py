def solve(n,array):
    def checkParity(a,b):
        if (a%2==0 and b%2==0) or (a&1 and b&1):
            return True
        return False
    count = 0
    if n == 1:
      return count
    for i in range(1,n):
        if checkParity(array[i-1],array[i]):
            count+=1
    return count




for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    print(solve(n,array))
