for _ in range(int(input())):
    n=int(input())
    if n==1 or n==3:
        print(-1)
    elif n==2:
        print(66)
    else:
        s=''
        for i in range(n-4):
            if i%2==0:
                s+='5'
            else:
                s+='0'
        s+='51'
        print(int(s)*66)