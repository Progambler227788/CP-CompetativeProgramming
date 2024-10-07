for _ in range(int(input())):
    row,column = map(int , input().split())
    ans = 0
    if row > column:
        ans = (row-1) ** 2 
        ans = ans + column if row & 1 else ans + (2 * row - column)
    else:
        ans = (column-1) ** 2 
        ans = ans + row if not column & 1  else ans + (2 * column - row)
    print(ans)

# for _ in range(int(input())):
#     x,y = map(int ,input().split())
    
        



    # 4 3-> 9 + (2 * 4 - 3) -> 9 + 5 -> 14 Even