with open('input1.txt') as f:
    lines = f.readlines()
    num,num1,num2,num3,maxcal = 0,0,0,0,0
    for line in lines:
        if line.strip():
            num = num + int(line)
        else:    
            if num > num1:
                num3 = num2
                num2 = num1
                num1 = num
            elif num > num2:    
                num3 = num2
                num2 = num
            elif num > num3:
                num3 = num            
            num = 0
    print(num1)
    print(num1 + num2 + num3)
