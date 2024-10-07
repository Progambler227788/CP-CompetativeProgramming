def maximizeNumberSum(number):
    return number if number==3 else 2

for _ in range( int(input())  ):
    print(maximizeNumberSum(int(input())))