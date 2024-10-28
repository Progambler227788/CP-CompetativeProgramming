def solve(n,array):
    # har element k right pa dekho usse ktny choty or barabar elements ha
    maxElements = 0
    for index,value in enumerate(array):
        current = 0
        for j in range(index, n ):
            if array[j] <= value:
                current+=1
        maxElements = max( maxElements, current)
    print(n - maxElements)

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    solve(n,array)
