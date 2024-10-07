
contain = {}

def canMakeEqual(s1, s2):
    # Write your code here
    first  = ''
    second = ''
    count = 0
    for i in range( len(s1)):
       print(first)
       print(second)
       if s1[i]!=s2[i] and second=='' and first=='' :
            count+=1
       elif s1[i]!=s2[i] and second!='' and first!='' and second!=s1[i] and first==s2[i]:
               return 0
       elif s1[i]!=s2[i] and second!='' and first!='' and second==s1[i] and first!=s2[i]:
                first =s1[i]
                second =s2[i]
       elif s1[i]!=s2[i] and second!='' and first!='' and second==s1[i] and first==s2[i]:
            if count == 2: # already swap done
               return 0
            count+=1
       elif s1[i]!=s2[i]:
         return 0
    return 1
s1 = input()
s2 = input()
canMakeEqual(s1,s2)