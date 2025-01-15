total = 0
for _ in range( int(input())):
    data = list( map( int , input().split() ))
    total += sum(data)
if total == 0:
    print("YES")
else:
    print("NO")