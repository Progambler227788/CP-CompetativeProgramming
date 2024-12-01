n = input()
data = set()
for i in n:
    data.add(i)
count = len(data)
# for a in data.values():
#     if a==1:
#         count+=1
# print(data)
# print(count)
print("CHAT WITH HER!" if not count&1 else "IGNORE HIM!")
        