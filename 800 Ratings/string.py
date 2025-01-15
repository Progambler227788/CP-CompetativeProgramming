
for _ in range(int(input())):
    data = set()
    a = input()
    b = input()
    if set(a) == set(b):
        print(len(a) if len(a)>len(b) else len(b))
    else:
      for i in b:
          data.add(i)
      count = 0
      for i in a:
          if i not in b:
             count+=1
      print(len(b) + count)

# a
# aa

# aa
# a