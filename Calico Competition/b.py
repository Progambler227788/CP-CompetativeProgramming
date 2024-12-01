for _ in range(int(input())):
    number = int(input())
    result = ''
    if number == 0:
        result = 'haha good one'
    elif number>=180:
        result ="canceled"
    else:
        inject = number // 10
        result = inject * "berkeley" + "time"
    print(result)
        
    
        