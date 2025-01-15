for _ in range(int(input())):
    n,digit = map(int, input().split())
    data = [1]
    if digit%3==0 or n>=3:
        data.append(3)
    if digit == 5:
        data.append(5)
    if digit==7 or n>=3:
       data.append(7)
    if digit==9 or ( n>=6 ) or (digit%3==0 and n>=3):
       data.append(9)
    print(*data)

#A number will be divisble by 3 if 
# if digit%3==0 or either total digis are greater than or equal to 6 of a specific digit give, n>=3
# A number will be divisble by 5 if end digit is 5 or 0 ,so d=0

# A number will be divisble by 9 if d is 9, n! is 9, or either d=3 and n!=3
# n>=6
# A number will be divisble by 9 if d is 7 or n>=3

