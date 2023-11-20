points = 0
with open('input2.txt') as f:
#with open('test1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if line == "A X": #rockrock 3 + 1
            points += 4
        elif line == "A Y": #rockpaper 6 + 2
            points += 8        
        elif line == "A Z": #rockscissors 0 + 3
            points += 3        
        elif line == "B X": #paperrock 0 + 1
            points += 1 
        elif line == "B Y": #paperpaper 3 + 2
            points += 5        
        elif line == "B Z": #paperscissors 6 + 3
            points += 9        
        elif line == "C X": #scissorsrock 6  + 1
            points += 7   
        elif line == "C Y": #scissorspaper 0 + 2
            points += 2        
        elif line == "C Z": #scissorsscissors 3 + 3
            points += 6          
print(points)            

points = 0
with open('input2.txt') as f:
#with open('test1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if line == "A X": ##rockscissors 0 + 3 
            points += 3
        elif line == "A Y": #rockrock 3 + 1
            points += 4        
        elif line == "A Z": #rockpaper 6 + 3
            points += 8        
        elif line == "B X": #paperrock 0 + 1
            points += 1 
        elif line == "B Y": #paperpaper 3 + 2
            points += 5        
        elif line == "B Z": #paperscissors 6 + 3
            points += 9        
        elif line == "C X": #scissorspaper 0  + 2
            points += 2   
        elif line == "C Y": #scissorsscissors 3 + 3
            points += 6        
        elif line == "C Z": #scissorsrock 6 + 1
            points += 7          
print(points)            