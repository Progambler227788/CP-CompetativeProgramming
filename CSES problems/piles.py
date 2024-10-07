

# when we reduce we make equations like
# 1 * X + 2 * Y = A
# 2 * X + 1 * Y = B
# Finding value of X and Y
# X = A - 2 / Y
#

def solve(a,b,dp={}):
    # 2 3 -> 0 2
    if a==0 and b==0:
       return "YES"
    if a<=0 or b<=0: 
       return "NO"
    if (a-1,b-2) not in dp:
        dp[(a-1,b-2)] = solve(a-1,b-2,dp)

    if (a-2,b-1) not in dp:
        dp[(a-2,b-1)] = solve(a-2,b-1,dp)

    c  =  dp[(a-1,b-2)]
    d  =  dp[(a-2,b-1)] 
    if d==c: # YES YES -> YES, NO NO -> NO
       return d
    # YES NO -> YES, NO YES -> YES
    return "YES"


    

    


for _ in range(int(input())):
    a,b= map(int , input().split())
    # print(solve(a,b))

        # positive and divisibility
    if ( (2* a - b)%3 == 0) and ( (2* b - a )%3 == 0) and ( (2*b - a )>=0 ) and ( (2* a - b )>=0 ):
        print("YES")
    else:
        print("NO")
    # if a%2==0 and b%2==0 or a==0 or b==0:
    #     print("NO")
    # else:
    #     print("YES")

        # 2 1,