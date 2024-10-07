def checkDivisibility(number):
    n = int(number)
    data = set(number)
    count = 0
    for i in data:
        if i =='0' or n % int(i) == 0:
           count+=1
    if count == len(data): return True 
    return False

for _ in range(int(input())):
    num = input()
    while not checkDivisibility(num):
          num = str( int(num) + 1)
    print(num)