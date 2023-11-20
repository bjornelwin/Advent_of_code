import numpy as np

if __name__ == '__main__':
    grid = np.zeros((1000,1000))
    len = 10
    Rope = [[500,500] for i in range(len)]
    dirs = {'R': [0,1], 'L': [0,-1], 'U': [1,0], 'D': [-1,0]}
    
    with open('input9.txt') as f:
        lines = f.readlines()
        for line in lines:
            dir, steps = line.rstrip().split()

            for i in range(int(steps)): 
                Rope[0][0] += dirs[dir][0]
                Rope[0][1] += dirs[dir][1]
                for j in range(0,len-1):

                    if np.sqrt((Rope[j][0]-Rope[j+1][0])**2 + (Rope[j][1]-Rope[j+1][1])**2) > np.sqrt(2):

                        if abs(Rope[j][1]-Rope[j+1][1])  <= 1:
                            Rope[j+1] = [int(Rope[j][0] - (Rope[j][0] - Rope[j+1][0])/2) , Rope[j][1]]   

                        elif abs(Rope[j][0]-Rope[j+1][0])  <= 1:  
                            Rope[j+1] = [Rope[j][0] , int(Rope[j][1] - (Rope[j][1] - Rope[j+1][1])/2)]   
                        
                        else:
                            Rope[j+1] = [int(Rope[j][0] - (Rope[j][0] - Rope[j+1][0])/2) , int(Rope[j][1] - (Rope[j][1] - Rope[j+1][1])/2)]   
        
                grid[Rope[len-1][0]][Rope[len-1][1]] = 1

    print(np.sum(grid))
    