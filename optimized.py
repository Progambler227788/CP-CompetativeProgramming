import sys
sys.stdout =  open('CP')

def griDSolving(grid):
    rows = len(grid)
    cols = len(grid[0])

    total_sum = 0
    total_abs_sum = 0
    count_negatives = 0
    min_abs_value = float('inf')
    has_zero = False

    for i in range(rows):
        for j in range(cols):
            value = grid[i][j]
            abs_value = abs(value)
            total_sum += value
            total_abs_sum += abs_value
            
            if value < 0:
                count_negatives += 1
            
            if value == 0:
                has_zero = True
            
            if abs_value < min_abs_value:
                min_abs_value = abs_value

    if count_negatives % 2 == 0 or has_zero:
        return total_abs_sum
    else:
        return total_abs_sum - 2 * min_abs_value

testCases = int(input())

for i in range(testCases):
    matrix = []
    n, m = map(int, input().split())
    for row in range(n):
        Row = [int(x) for x in input().split()]
        matrix.append(Row)
    print(griDSolving(matrix))
