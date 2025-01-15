# dealing the K damage to monsters with highest power
'''  

3
3 2
1 2 3
2 3
1 1
4 3
2 8 3 5


3 2 1 , damage is 2
1 2 1,  damage is 2
1 0 1

'''

for _ in range(int(input())):
    n,k = map(int , input().split())
    powers = list(map(int , input().split()))
    for i in range( n ):
        data = powers[i]%k 
        powers[i] = data if data!=0 else k 
    ord_data = [ (powers[i], i+1 ) for i in range( n ) ]
    # sort the data by values 
    ord_data.sort( key= lambda x : -x[0])
    print(*[ord_data[x][1] for x in range(n)])
    