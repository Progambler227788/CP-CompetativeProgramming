def swappingFirstCharacters(a,b):
    print(b[0]+a[1:],a[0]+b[1:])

for _ in range( int(input())  ):
    A,B = input().split()
    swappingFirstCharacters(  A,B  )