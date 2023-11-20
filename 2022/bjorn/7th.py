def dircount(layers, dir):
    sum = 0
    for d in  layers[dir]['dirs']:
        sum += dircount(layers,d)
    return sum + layers[dir]['dirsize']

if __name__ == '__main__':
    layers = {}
    updir = None
    with open('input7.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip().split()
            if len(line) == 3:
                if line[2] == '..':
                    updir = layers[updir]['updir']
                else:            
                    layers[line[2]] = {
                        'dirsize' : 0,
                        'dirs' : [],
                        'updir' : updir
                    }
                    if updir is not None:
                        layers[updir]['dirs'].append(line[2])
                    updir = line[2] 

            elif line[0].isdigit():
                layers[updir]['dirsize'] += int(line[0])
            
        totsum = sum([ s if s<=100000 else 0 for s in [dircount(layers, key) for key in layers]])
        
        print(totsum)      
        