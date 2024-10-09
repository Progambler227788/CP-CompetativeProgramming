def extremeRound(n):
    count = 0
    while n>0:
          dig = n%10
          if dig>=1:
               count+=1
          if count==2:
             return False
          n//=10
    return True


# 999999
def solve(n):
    count = 0
    maping = {}
    i = 1
    # increment = 1
    # while i<=n:
    #     if extremeRound(i):
    #         count+=1
    #         print(i)
    #     maping[i] = count
    #     if i == n:
    #        i*=1
          
    for i in range(1,n+1):
        if extremeRound(i):
            count+=1
            # print(i)
        maping[i] = count

    return maping
data = solve(999999)

for _ in range(int(input())):
    print(data[int(input())])
    
        