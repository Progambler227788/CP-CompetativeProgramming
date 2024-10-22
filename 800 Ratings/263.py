# distance = 0
row = 0
col = 0
for _ in range(5):
    data = list(map(int , input().split()))
    if 1 in data:
        row = _
        col = data.index(1)
r = abs(row - 2)
c = abs(col - 2)
print(r+c)
    