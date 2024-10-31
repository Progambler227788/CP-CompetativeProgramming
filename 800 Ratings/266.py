def solve(n,data):
    count = 0
    for i in range(1,n):
        if data[i]==data[i-1]:
            count+=1
    print(count)

n = int(input())
string = input()
solve(n,string)
