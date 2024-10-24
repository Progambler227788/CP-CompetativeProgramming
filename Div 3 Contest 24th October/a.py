def solve(n):
    if n&1:
        print("Kosuke")
    else:
        print("Sakurako")

for _ in range(int(input())):
    n = int(input())
    solve(n)

