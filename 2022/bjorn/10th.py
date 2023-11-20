import numpy as np

def draw(cycle, pos , screen):
    row = int(np.floor((cycle)/40))
    col = int(cycle - row*40)
    if col in [pos -1, pos , pos +1]:
        screen[row][col]= '#'
    return screen

checkpoints = [20, 60, 100, 140, 180, 220]
cycle = 0
sum = 1
totsum = 0
screen = [['.' for i in range(40)] for i in range(6) ]

screen = draw(cycle,sum,screen) 
cycle += 1   
with open('input10.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip().split()
        
        
        if cycle in checkpoints:
            totsum += cycle * sum
        
        cycle += 1
        screen = draw(cycle,sum,screen)    
        
        if len(line) == 2:
            if cycle in checkpoints:
                totsum += cycle * sum

            sum += int(line[1])
            cycle +=1
            screen = draw(cycle,sum,screen) 

for line in screen:
    print(line)
            
print(totsum)
            