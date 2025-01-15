id = {}
for _ in range(int(input())):
    n = input()
 
    if n in id:
        id[n] = id[n] + 1
        print(n + str(id[n]))
    else:
        id[n] = 0
        print("OK")
