for _ in range(int(input())):
    n,k = map(int , input().split())
    arr = list(map(int , input().split()))
    index = -1
    for i in range(n):
        check = -1
        for j in range(n):
            if i!=j:
               if abs(arr[i]-arr[j])%k==0:
                  check = 10 # not win
                  break
        if check == -1:
           index = i
           break
    if index!=-1:
        print("YES")
        print(index+1)
    else:
        print("NO")

   