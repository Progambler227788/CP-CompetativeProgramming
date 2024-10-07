import math
from functools import reduce

def factors(n):    
    return list(sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))


def getLargestDivisor(a,b):  
    
    for number in range( b+1, 10**9 ):
     divisors = factors(number) 
     if divisors and divisors[-2] == b and divisors[-3] == a:
         print(number)
         break
               
    

def main():
    testCases = int(input())
    for t in  range(testCases):
         # Read number of students
        s = input()
        s = s.split()
        a = int(s[0])
        b = int(s[1])
        getLargestDivisor(a,b)
main()