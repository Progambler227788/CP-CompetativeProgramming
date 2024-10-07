def check(array,n):
    # n = len(array)

    # as increasing as mean usky barabar lana ha

    # replace or swap b krty jana ha
    
    moves = 0

    for i in range(n-1):
        if array[i+1] < array[i]:
           temp = array[i] - array[i+1]
           moves += temp
           array[i+1] = array[i+1] + temp
    return moves
n = int(input())
array = list(map(int, input().split()))
print(check(array,n))