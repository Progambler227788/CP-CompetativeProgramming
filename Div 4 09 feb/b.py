for _ in range(int(input())):
    data = input()
    total = len(data)
    for i in range(total-1):
        if data[i]==data[i+1]:
            total = 1
            break
    print(total)
            