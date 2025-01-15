n = input()
data = set(n)
output='NO'
if len(data)==2 and '4' in data and '7' in data:
    output = 'YES'
inti = int(n)
if inti%4==0 or inti%7==0 or inti%47==0 or inti%74==0:
   output = 'YES'
   
print(output)
   