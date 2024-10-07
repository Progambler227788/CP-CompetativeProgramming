def solve(n,array):
    # bara ko sab se chota is trha chalaty chalaty jao
    # I tried even then odd logic
    # I tried using sorted array 
    # then I just got random thought and thought just map smallest to largest and largest to smallest and go on
    # 1 2 3 4 5 mappe dto 5 4 3 2 1
    arr = sorted(array) # sort the array
    indexes = {}
    for index,element in enumerate(array):
        indexes[element] = index
    # print(indexes)
    maping = [0] * n
    # print(maping)
    right = -1
    for i in arr:
        maping[ indexes[i] ] = arr[right]
        right += -1
    print(*maping)

for _ in range(int(input())):
    n = int(input())
    array = list( map(int, input().split()) )
    solve(n,array)