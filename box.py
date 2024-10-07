import sys
sys.stdout = open('D:/CP/output.txt','w')
sys.stdin = open('D:/CP/input.txt','r')

def takeSum(grid,rows,cols):
    total = 0
    for i in range( rows ):
        for j in range( cols ):
            total += grid[i][j]
    return total
    
def takeSumAbs(grid,rows,cols):
    total = 0
    for i in range( rows ):
        for j in range( cols ):
            total += abs(grid[i][j])
    return total

def takeMinimum(grid,rows,cols):
    miniMum = 3000
    allSame = grid[0][0] # compare if elements are same
    count = 0
    total = 0
    for i in range( rows ):
        for j in range( cols ):
            if abs(grid[i][j]) < abs(miniMum):
               miniMum = grid[i][j]
            if abs(grid[i][j]) == abs(allSame):
               count+=1
            total += 1
    if total == count:
       return -3000
    return miniMum # as we need positive value so that we can subtract it afterwards


def griDSolving(grid):
    rows = len(grid) # total rows
    cols = len(grid[0]) # total columns
    countNegatives = 0
    miniMum = takeMinimum(grid,rows,cols)
    has_Zeros = False
    for i in range( rows ):
        for j in range( cols ):
            if grid[i][j] < 0:
                countNegatives +=1 # count negative numbers
            elif grid[i][j] == 0:
                 has_Zeros = True

    our_final_sum = takeSum(grid,rows,cols)
    if countNegatives%2 == 0 or has_Zeros==True: # even 
       return  takeSumAbs(grid,rows,cols)
    
    if miniMum == -3000:
       return our_final_sum
    if miniMum < 0:  # in case it was added so we have to subtract it as - will be ther so +,i is -
        return takeSumAbs(grid,rows,cols) + miniMum + miniMum  # remove it 2 times as our total sum has added it first, so removing it will result 0 value of it and again 
    # print(miniMum)
   # similary here we have added 1 to result but minise would also need to be don
    return takeSumAbs(grid,rows,cols) - miniMum - miniMum# in case element positive so - will got it due to odd minus signs 



testCases = int(input())


for i in range(testCases):
    matrix = []
     # Read n and m from the first line
    n, m = map(int, input().split())
    for row in range(n):
        Row = [int(x) for x in input().split()]
        matrix.append(Row)
    print(  griDSolving(matrix) )
    
