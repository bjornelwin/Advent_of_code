if __name__ == '__main__':
    forest = []
    with open('input8.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            treerow  = []
            for tree in line:
                treerow.append(int(tree))
            forest.append(treerow)
        visiblemap = [[0 for i in range(len(forest[0]))] for i in range(len(forest)) ]    
    
    # look down
    maxdown = [-1 for i in range(99)]
    maxup = [-1 for i in range(99)]
    maxleft = [-1 for i in range(99)]
    maxright = [-1 for i in range(99)]
    for idx1 in range(99):
        for idx2 in range(99):
            if forest[idx1][idx2] > maxright[idx1]:
                visiblemap[idx1][idx2] = 1
                maxright[idx1] = forest[idx1][idx2]           
            if forest[idx1][98 - idx2] > maxleft[idx1]:
                visiblemap[idx1][98-idx2] = 1
                maxleft[idx1] = forest[idx1][98 - idx2]
            if forest[idx2][idx1] > maxdown[idx1]:
                visiblemap[idx2][idx1] = 1
                maxdown[idx1] = forest[idx2][idx1]
            if forest[98-idx2][idx1] > maxup[idx1]:
                visiblemap[98 - idx2][idx1] = 1
                maxup[idx1] = forest[98 - idx2][idx1]    
    visibletrees = sum([s for s in [sum(row) for row in visiblemap]])
    print(visibletrees)


    visiblemap2 =  [[0 for i in range(len(forest[0]))] for i in range(len(forest)) ]  
    for row in range(99):
        for col in range(99):
           
            tree = forest[row][col]
            right,left,up,down = 0,0,0,0
            for r in range(row): #right
                right += 1
                if tree <= forest[row -r -1][col]:
                    break

            for r in range(98 - row): #left
                left += 1
                if tree <= forest[row + r +1][col]:
                    break
                
            for c in range(col): #up
                up += 1
                if tree <= forest[row][col -c-1]:
                    break

            for c in range(98 - col): #down
                down += 1
                if tree <= forest[row][col+c+1]:
                    break
            visiblemap2[row][col] = right*left*up*down
    print(max([max(row) for row in visiblemap2]))
        