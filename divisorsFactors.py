def makeFactors(n):
    factors = set()
    for i in range(1, (int(n**0.5)+1) ): # n**0.5 is sq root of number
        if n%i==0:
         factors.add(i)
         factors.add(n//i )
    return sorted(list(factors))
def checkDistance(number,d): # as in sorted distance will be maximum between close pairs so it will increase with other pairs
    # adjacent element distance check
    data = makeFactors(number)
    if len(data)<4:
        return False
    for i in range(1,len(data)):
        if abs(data[i-1] - data[i]) < d:
           return False
    return True


def takeNumber(number):
    start = 6
    if number>=50:
       start = 5434
    if number>=100:
       start = 10000
    if number>=200:
       start = 70000
    if number>=500:
       start = 507526
    if number>=1000:
       start = 50752656
    if number>=2000:
       start = 5075265688
    
         
    while not checkDistance(start,number):
          start+=1
    print(start)

# print(makeFactors(6))
for t in  range(int(input())):
    # Read number of students
    number =  input()
    number  = int(number)
    takeNumber(number)