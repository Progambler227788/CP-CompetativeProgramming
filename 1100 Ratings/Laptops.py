# laptops={}
n = int(input())
mess = "Poor Alex"
mini,maxi = float('inf'),float('-inf')
for _ in range(n):
    a,b = map( int , input().split())
    if a>mini and b<maxi:
            mess = "Happy Alex"
            break
    mini = min(a,mini)
    maxi = max(b,maxi)
    # if laptops:
    #     laptops[a]=b
    #     for key,value in laptops.items():
    #     #    print('here')
    #        if a>key and b<value:
    #            mess = "Happy Alex"
    #            break
    #     if mess == "Happy Alex":
    #        break

    # else:
    #     laptops[a]=b
        
        
# print(laptops)
              
print(mess)


#