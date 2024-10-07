# import sys
# sys.stdout = open('D:/CP/output.txt','w')
# sys.stdin = open('D:/CP/input.txt','r')

def predictShuffle(students,sizes):
    count=0
    compare = sizes[0]
    for i in range(students):
        if sizes[i] == compare:
           count+=1

    if count != students:
       print(-1)
    else:
        newData = [students] + [x for x in range(1,students)] # 5 students thy then 5 + 1,2,3,4
        print(*newData)
    
    
      

testCases = int(input())

for t in  range(testCases):
     # Read number of students
    students =  input()
    students = int(students)
    # read their total sizes, 0 index -> 1 , 1 index -> 1 so on
    taken = input() # taken as input string
    sizes = taken.split() # spaces removed
    for i in range(len(sizes)):
        sizes[i] = int(sizes[i])
    predictShuffle(students,sizes) 
    
