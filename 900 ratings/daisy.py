# removing first occurence of character

from collections import defaultdict
def take(word1,word2):
    # store frequencies
    f1,f2 = defaultdict(int), defaultdict(int)
    for i in word2:
        f2[i]+=1
    mading = [] 
    for i in word1:
        if i in f2:
           mading.append(i)
           f1[i]+=1
    
    # remove word1<word2
    answer="YES"
    for i in word2:
        if f2[i]>f1[i]:
            answer = "NO"
            break
    if answer=="YES":
        # print(mading)
        for i,v in f1.items():
            # took = max(f1[i],f2[i])
            counter = f1[i]-f2[i]
            for _ in range(counter):
                if i in mading:
                   mading.remove(i)
    conv = "".join(mading)
    # print(conv)
    if conv!=word2:
        answer="NO"
    return answer

for _ in range(int(input())):
    word1,word2 = map(str, input().split())
    print(take(word1,word2))
    
            
    