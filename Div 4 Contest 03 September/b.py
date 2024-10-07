def a1(array):
    integer = 1
    for i in array:
        if i == '#':
           break
        integer+=1
    return integer

for _ in range(int(input())):
    total = int(input())
    data = []
    for _ in range(total):
        array = input() # read as stirng
        data.append( a1(array) )
    for i in data[::-1]:
        print(i,end=" ")

    
