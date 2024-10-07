
def solve(n,arr):
    arr = sorted(arr)
    # by sorting we can compare first and last elements to check if array has same elements 
    if arr[0] ==arr[-1]:
        print(-1)
        return
    # checker = True
    element = arr[0]
    count = 0
    while arr[count] == element:
        count+=1

    # B divides A, smallest number will not be divided by big number
    # for index in range(n):
    #     told = True
    #     count = 1
    #     for previous in range(n):
    #         if previous!=index and arr[previous] % arr[index] == 0:
    #            if arr[previous] == arr[index]:
    #               count+=1
    #            else:
    #              told = False
    #              break
    #     if told:
    #         element = arr[index]
    #         for i in range(count):
    #             c.append(element)
    #         for i in arr:
    #             if element!=i:
    #                 b.append(i)
    #         # b = arr[0:index] + arr[index+1::]
    #         break
    # if told:
    #    b = arr[: n//2]
    #    c = arr[n//2::]
    # if len(c) == 0 or len(b)==0: # 1 3 5
    #    print(-1)
    #    return
    print(f"{count} {n - count}")
    print(*arr[:count])
    print(*arr[count::])
    # print(*b)
    # print(*c)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n,arr)

