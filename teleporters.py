
# import sys
# sys.stdout = open('D:/CP/output.txt','w')
# sys.stdin = open('D:/CP/input.txt','r')

def takeInput(size,array,coins):
    teleporters = 0
    # sortedData = sorted(array) # always take minimum from here

    inventory= {}
    for index,element in enumerate(array,start=1):
        inventory[index] = (index) + element

    inventorySorted = dict( sorted(inventory.items(), key=lambda item:item[1]))

    # print(inventorySorted)
             
    for data in inventorySorted.values():
        coins-=data
        if coins<0:
            break
        else:
          teleporters+=1

    return teleporters


for _ in range(int(input())):
    size, coins = map(int,input().split())
    array = list(map(int,input().split()))
    print(takeInput(size,array,coins))

