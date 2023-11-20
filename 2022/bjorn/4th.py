sum  = 0
with open('input4.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        dash = int(line.find('-'))
        dash2 = int(line.find('-',dash+1))
        comma = int(line.find(','))
        a,b,c,d = int(line[:dash]), int(line[dash+1:comma]),int(line[comma+1:dash2]), int(line[dash2+1:])
        first = set(range(a, b+1))
        second = set(range(c,d+1))
        if (first & second) == first or (first & second) ==second:
            sum +=1
print(sum)

sum  = 0
with open('input4.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        dash = int(line.find('-'))
        dash2 = int(line.find('-',dash+1))
        comma = int(line.find(','))
        a,b,c,d = int(line[:dash]), int(line[dash+1:comma]),int(line[comma+1:dash2]), int(line[dash2+1:])
        first = set(range(a, b+1))
        second = set(range(c,d+1))
        if len(first & second) is not 0: 
            print(first & second)
            sum +=1
print(sum)