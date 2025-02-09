a,b,c = int(input()),  int(input()),  int(input())

p,q,r,j,e = a+b*c,a*(b+c), (a+b)*c, a*b*c,a+b+c
print(max(max(max(max(p,q),r),j),e))
