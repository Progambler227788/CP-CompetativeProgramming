def printDigitsSum(number):
    sum_taken = 0
    while number>0:
          sum_taken += number%10
          number//=10
    print(sum_taken)

for _ in range( int(input())  ):
    printDigitsSum(int(input()))
