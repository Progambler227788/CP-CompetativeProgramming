def solve(columns,array):

    def bfs(i,j,array):
        que = [(i,j)]
        rows = 2
        visited = set([(i, j)]) 
        directions = [
        (1, 0),   # Down
        (-1, 0),  # Up
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 1),   # Bottom-right (Diagonal)
        (-1, -1), # Top-left (Diagonal)
        (-1, 1),  # Top-right (Diagonal)
        (1, -1)   # Bottom-left (Diagonal)
    ]

        while que:
            u,v = que.pop(0)
            # print(u,v)
            if not (0 <= u < rows and 0 <= v < columns):
               continue
            if u == 1 and v == columns -1:
               return True
            
            for du, dv in directions:
                new_u, new_v = u + du, v + dv
            
                if 0 <= new_u < rows and 0 <= new_v < columns and array[new_u][new_v] == 0 and (new_u, new_v) not in visited:
                 visited.add((new_u, new_v))  # Mark as visited
                 que.append((new_u, new_v))
          
        return False
    return bfs(0,0,array)

for _ in range(int(input())):
    cols = int(input())
    data = input()
    array = []
    a1 = [int(char) for char in data]
    array.append(a1)
    data = input()
    a1 = [int(char) for char in data]
    array.append(a1)
    # print(array)
    if solve(cols,array):
        print("YES")
    else:
        print("NO")

           

