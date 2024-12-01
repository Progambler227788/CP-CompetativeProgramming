def checker(number):
    data = set()
    while number>0:
          digit = number%10
          if digit in data:
              return False
          data.add(digit)
          number//=10
    return True
    

preProcessed = list()
for i in range(1000,9013):
    if checker(i):
        preProcessed.append(i)
year = int(input())
took = 999
for y in preProcessed:
    if y > year:
        took = y
        break
print(took)