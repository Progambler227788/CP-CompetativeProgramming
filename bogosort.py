def takeArray(data):
    data = sorted(data,reverse=True)
    print(*data)


testCases = int(input())
# read test cases 
for t in  range(testCases):
    # Read number of students
    size =  input()
    size  = int(size)
    takeArray(map(int, input().split()))