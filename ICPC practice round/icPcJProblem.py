totalPersons = 0
for _ in range(int(input())):
    s = input()
    event,count = s[0], int(s[2:])
    yes = 'NO'
    if event == 'B':
        totalFrees = count
        diff = totalPersons - totalFrees
        # print(diff)
        if diff < 0: # total free seats zada agai
           totalPersons = 0 # sab chalay gaye
           # hico b jaye ga
           yes = 'YES'
        else: # sab chaly gaye ya koi reh gaya tu hico ni ja skta
            totalPersons = diff
        print(yes)                   
    elif event == 'P':
        totalPersons+=count
        
    