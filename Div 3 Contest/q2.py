

def giveCost(n,string):
    operations = 0
    if n ==1:
        return 1
    if n ==2:
        return 0
    evenElements = {}
    oddElements =  {}
    for i in range(n) :
        if i%2==0:
           if string[i] in evenElements:
               evenElements[string[i]].append(i)
           else:
               evenElements[string[i]] = [i]
        else:
            if string[i] in evenElements:
               oddElements[string[i]].append(i)
            else:
                oddElements[string[i]] = [i]
    replacements = 0
    sorted_evens =  sorted(evenElements, key= lambda x : len(x[1]) )
    for key, positions in sorted_evens [:-1]:
        if key in oddElements:
            oddSize = len(oddElements[key])
            evenSize = len(evenElements[key])
            replacements+=


               
              
            

for _ in range(int(input())):
   n = int(input().split())
   string = input()
   
   