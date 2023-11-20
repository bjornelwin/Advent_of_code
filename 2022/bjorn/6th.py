

n =4  
l = ['']*n
pos = 0
with open('input6.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        for char in line:
            for i in range(0,n-1):
                l[i] = l[i+1]
            l[n-1] = char
            pos += 1
            if len(set(l)) == n:
                    if l[0] is not '':
                        print(pos)
                        print(l)
                        break 
            
        

# c1,c2,c3,c4 = '','','',''
# pos = 0
# i = 0
# with open('input6.txt') as f:
    # lines = f.readlines()
    # for line in lines:
        # line = line.rstrip()
        # for char in line:
            # i += 1
            # c1,c2,c3,c4 = c2,c3,c4,char
            # if len(set(c1+c2+c3+c4)) == 4:
                    # print(set(c1+c2+c3+c4))
                    # print(i)
                    # break 
            
        
