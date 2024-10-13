# way too long words

for _ in range(int(input())):
    data = input()
    n = len(data)
    if n>10:
       print(f"{data[0]}{n-2}{data[-1]}")
    else:
        print(data)