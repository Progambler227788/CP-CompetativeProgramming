from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = defaultdict(int)
    for index,ele in enumerate(s):
        freq[ele]+=1
    data = list(s)
    maxi = None
    mini = None
    max_freq = max(freq.values())
    min_freq = min(freq.values())

    for index, char in enumerate(s):
      if freq[char] == max_freq and maxi is None:
        maxi = index
      if freq[char] == min_freq and mini is None:
        mini = index
      if maxi is not None and mini is not None:
        break
    if maxi==mini:
      m = data[maxi]
      for i in range(n):
          if data[i] != m:
              data[i] = m
              break
    else:
        data[mini]= data[maxi]
    k = ''.join(data)
    print(k)
            
           
    
    