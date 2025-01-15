
for _ in range(int(input())):
    string = input()
    lid = list(string)
    lid.reverse()
    for index in range( len(lid) ):
        if lid[index] == 'p':
           lid[index] = 'q'
        elif lid[index]=='q':
            lid[index] = 'p'
    print(''.join(lid))