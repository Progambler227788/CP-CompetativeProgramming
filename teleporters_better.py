
# import sys
# sys.stdout = open('D:/CP/output.txt','w')
# sys.stdin = open('D:/CP/input.txt','r')

# Thoughts

# During this problem first I thought of minimum but was not forming logic like which minimum to pick as there are duplicates
# then after 2-3 hours of brainstorming, figuring out greedy concepts that somehow helped me, I thought myself like what test cases are demanding
# I tested each input/output on paper, so what I did I was picking minimum element from an array and then adding its distance and element and finally that add up value
# subtracted from coins but that was wrong why? So, reason is minimum element could be at the end of list and some element like minimum+1 may perform better
# so then what I did I made map like finding distance + element value and storing it at specific index starting from 1, but then major greedy technique worked in my mind
# it was useless to store indexes, eventually I made list to store only element+distance and then picking from start as it is in sorted order
# So, no need to delete, no need of boolean, no need of iterating all combinations
# Just storing and Sorting worked for me

def takeInput(size,array,coins):
    teleporters = 0
    # sortedData = sorted(array) # always take minimum from here

    inventory= []
    for index,element in enumerate(array,start=1):
        inventory.append((index) + element)

    inventorySorted = sorted(inventory)

    # print(inventorySorted)
             
    for data in inventorySorted:
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

