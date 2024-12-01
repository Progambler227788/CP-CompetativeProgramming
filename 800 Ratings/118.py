string = input()
data = ("a","e","o","u","i","y","A","E","O","U","I","Y")
result =""
for i in string:
    if i not in data:
       result+="."+ i.lower()
print(result)