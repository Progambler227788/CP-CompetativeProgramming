
def giveLength(current):
    if len(current) == 1:
       return 1
    
    data = set()
    ans = 0
    for i in current:
        data.add(i)
        ans += len(data)

    # count = 0

             
    return ans

          
# def giveLength1(current):
#     data = set()
    
#     def dfs(string):
#         if string in data:
#             return
#         data.add(string)
#         if len(string) <= 1:
#            return
#         # as greater than 1 hi hugi agr upr wali na chali
       
#         dfs(string[1:]) # skip first element
#         dfs(string[0] + string[2:])
        
    
#     dfs(current)
    
#     return len(data)

for _ in range(int(input())):
     n = int(input())
     string = input()
     
     print(giveLength(string))
