
def solve(a,b,taken):
    if a==b==taken: # 1 1 1, 2 2 2
       return "YES"
    if a==taken or b==taken:
       return "NO"
    rem = taken - a
    if rem-b<=1:
       return "NO"
    return "YES"

for _ in range(int(input())):
  n,a,b= map(int, input().split())
  print(solve(a,b,n))

  # 2 2 2

''' 
5 1 2 -> 1 2 3 4 5,  1 3 2 4 5
4 1 2 -> 1 2 3 4,   1 2 4 3
4 1 2

1 2 3 4
1 3 2 4


1 2 3 4 5 6
1 2 4 3 5 6

1 2 3
1 3 2
2 3 1
2 1 3
3 1 2
3 2 1

1 2 3 4
1 2 4 3
2 1 4 3  -> 4/2 is 2
1 3 2 4
1 3 4 2
1 4 3 2
1 4 2 3

3/2 -> 1
4/2 -> 2
6/2 -> 3
2 -> 1 2, 2 1

1 2 3 4 5
1 3 2 4 5
1 2 4 3 5

1 2 3 4 5 6
1 2 4 3 5 6



'''

  