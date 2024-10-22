def petyaStrings():
    a,b = input().upper(),input().upper()
    value = 0
    for index in range(len(a)):
        if a[index] < b[index]:
            value = -1
            break
        elif a[index] > b[index]:
            value = 1
            break
    print(value)
petyaStrings()