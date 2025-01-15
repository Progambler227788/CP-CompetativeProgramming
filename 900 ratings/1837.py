# count consectives less than and also greater than
for _ in range(int(input())):
    n = int(input())
    s = input()
    maxRepeat = 0
    initial = 1
    for i in range(1,n):
        if s[i-1] == s[i]:
            initial+=1
        else:
            maxRepeat = max(initial,maxRepeat)
            initial = 1
    maxRepeat = max(initial,maxRepeat)
    print(maxRepeat+1)