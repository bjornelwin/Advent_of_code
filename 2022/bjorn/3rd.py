point = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
with open('input3.txt') as f:
    lines = f.readlines()
    for line in lines:
        
        line = line.rstrip('\n')
        s1,s2 =  line[:int(len(line)/2)], line[int(len(line)/2):]
        a = set(s1)&set(s2)

        for char in a:
            sum += int(point.find(char))
print(sum)          

# 3b
point = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
with open('input3.txt') as f:
    lines = f.readlines()
    i = 0
    line1, line2, line3 = 0, 0 ,0
    for line in lines:
        if i % 3 == 0: 
            line1 = line.rstrip('\n')
        elif i % 3 == 1:
            line2 = line.rstrip('\n')
        else:
            line3 = line.rstrip('\n')
            a = set(line1)&set(line2)&set(line3)
            for char in a:
                sum += int(point.find(char))
        i+=1            
print(sum)          
