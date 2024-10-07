import sys

sys.stdout = open('output.txt', 'w')  
sys.stdin = open('subsonic_subway_input.txt', 'r')



for _ in range(int(input())):
    n = int(input())
    min_speed = 0.0
    max_speed = float('inf')
    yes = True
    for i in range(1,n+1):
        a,b = map(int,input().split())
        mini = i/b if b!= 0 else float('inf') 
        maxi = i/a if a!=0 else  float('inf') 
        if mini > max_speed:
            yes = False
        min_speed = max(mini,min_speed)
        max_speed = min(maxi,max_speed)
    if not yes or min_speed>max_speed:
       print(f"Case #{_+1}: {-1}")
    else:
       print(f"Case #{_+1}: {min_speed:.6f}")


        


