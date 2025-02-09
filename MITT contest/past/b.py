n = int(input())
array = list(map(int , input().split()))
data = sorted(array)
x = n//2
# if n&1:
#     print(data[x])
# else:
print(data[x+1])

    