# A. Don't Try to Count


# as it is ( n⋅m≤ 25)

# n =1, m =25, 1<= n*m <=25
# so if n is and m is 25, then maximum operations we will have
# like i've t and other is t but 25 t's are there
# first operation tt,, 2
# second opeation tttt,, 4
# third operation,,, 8
# fourth ,,,, 16
# fifth ,,, 25
# so max operation is 5 

# Big O(6 * (2^5 * n * m)) ||||||||||||||||||||||||||  (2^5 * n * m)) -> searching 
def makeIt(x,y):
    operations = 0
    for i in range(10):
        if y in x:
           return operations
        operations+=1
        x+=x
    return -1

for _ in range(int(input())):
    a,b = map(int, input().split())
    x,y = input(),input()
    print(  makeIt(x,y))