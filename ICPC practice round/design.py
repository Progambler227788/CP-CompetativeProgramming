# same design start we_swapped or end pa agr 1 righting building koi uska dusra ni tu center we_swapped daly gy
# 
# arcacer
# racacer 1
# raccear 2
# racecar 1
# letelt
# tleelt moved t 2 times

# slicing
from collections import defaultdict
def solving(s):
    string = list(s)
    m = 0
    maping = defaultdict(int)
    for im in string:
        maping[im]+=1
    od = 0
    for i in maping.values():
        if i & 1:
            od+=1
    if od>1:
        print(-1)
        return 
    m = 0
   
    while left < right:
        if s[left] == s[right]:  # If characters are the same, no move needed
            left += 1
            right -= 1
        else:
            # Find a matching character from the right side
            r = right
            while r > left and s[left] != s[r]:
                r -= 1

            if r == left:  # If no match found, swap with the middle element
                s[left], s[(len(s) // 2)] = s[(len(s) // 2)], s[left]
                moves += 1
            else:
                # Move the character from right to its correct position
                while r < right:
                    s[r], s[r + 1] = s[r + 1], s[r]
                    r += 1
                    moves += 1
                left += 1
                right -= 1

    print(m)    

for _ in range(int(input())):
    ping = input()
    solving(ping)
           