testcases  = int(input())
threshold = int(input())
for _ in range(testcases):
    n = int(input())
    array = list(map(int, input().split())) 
    differences = []
    gg = len(array)
    for index in range( gg - 1 ):
        differences.append( abs(array[index]  - array[index+1]  ))
    gg = len(differences)
    pushed = []
    # print(differences)
    for index in range( gg - 1 ):
        took =  abs(differences[index]  - differences[index+1]  )
        if took<threshold:
            pushed.append(0)
        else:
            pushed.append(1)
    print(*pushed)