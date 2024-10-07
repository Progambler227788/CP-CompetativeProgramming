for _ in range(int(input())):
    a,b,c = map(int, input().split())
    if a==b and c & 1:
       print("First")
    elif a==b:
       print("Second")
    elif a<b:
       print("Second")
    else:
       print("First")