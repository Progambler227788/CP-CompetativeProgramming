for _ in range(int(input())):
    string = input()
    result = ''
    if string.startswith("o"):
        result = "CALICO" + string[1:]
    elif string.startswith("co"):
          result = "CALICO" + string[2:]
    elif string.startswith("ico"):
          result = "CALICO" + string[3:]
    elif string.startswith("lico"):
          result = "CALICO" + string[4:]
    elif string.startswith("alico"):
          result = "CALICO" + string[5:]   
    elif string.startswith("calico"):
        result = "CALICO" + string[6:]
    else:
        result = string
    print(result)
        
    
        