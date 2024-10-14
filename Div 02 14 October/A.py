def solve(n,r,array):
    seats = r * 2 
    totalMembers = 0
    rem = 0
    for i in array:
        if i%2==0:
           seats-=i
           totalMembers+=i
        else:
           seats-= (i-1)
           totalMembers+=i-1
           rem+=1
    if rem*2 <=seats:
       totalMembers += rem
    else:
       totalMembers += seats - rem
    print(totalMembers)

# 6 seats
# remaining 2
# 12 seats
# 8 member

    

for _ in range(int(input())):
    n,r = map(int , input().split())
    array = list(map(int , input().split()))
    solve(n,r,array)

# 4 5 -> 
# 10
# 2, 4 satisfy
