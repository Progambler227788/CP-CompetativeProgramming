# def fairNess(number):
#     check = number
#     count = 0
#     yes=0
#     while number>0:
#         digit = number%10
#         if digit!=0 and check%digit == 0:
#            yes+=1
#         count+=1
#         number//=10
#     return yes == count


# this is better because it avoids already checked digits, convert to string and then simply set 
def fairNess(number):
    str_num = str(number)
    unique_digits = set(str_num)  
    
    for digit in unique_digits:
        if digit == '0':  
            continue
        if number % int(digit) != 0:
            return False
    return True
            

def takeNumber(data):
    minimumNumber = data
    # print(fairNess(minimumNumber))
    while not fairNess(minimumNumber):
        minimumNumber+=1
    print(minimumNumber)
    


testCases = int(input())
# read test cases 
for t in  range(testCases):
    # Read number of students
    number =  input()
    number  = int(number)
    takeNumber(number)
    