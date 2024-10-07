def solve(n,array):
    xor = 0

    for i in array:
        xor^=i
    if n & 1:
        return xor
    if xor == 0:
        return array[-1]
    return -1

# xor of all elements is dependent on x in case of odd or not dependent in even case
# x ^ x ^ x is x
# x ^ x ^ x ^ x is always 0

for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    print(solve(n,array))