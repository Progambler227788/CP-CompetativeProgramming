# two screens

# just compare first equal characters and then just find remaining un matching characters
def solve(a,b):
    n1,n2 = len(a),len(b)
    matching = 0
    iterations = min(n1,n2)
    for i in range(iterations):
        yes =  int( a[i] == b[i])
        if yes == 0:
            break
        matching += yes
    t1 = n1 - matching
    t2 = n2 - matching
    calc = t1+t2
    # abcde aghej -> a, copy, 
    if matching>=1:
        print(calc+matching+1)
    else:
        print(calc)
for _ in range(int(input())):
    a,b = input(),input()
    solve(a,b)