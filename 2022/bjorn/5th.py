piles = {
    '1': 'HTZD',
    '2': 'QRWTGCS',
    '3': 'PBFQNRCH',
    '4': 'LCNFHZ',
    '5': 'GLFQS',
    '6': 'VPWZBRCS',
    '7': 'ZFJ',
    '8': 'DLVZRHQ',
    '9': 'BHGNFZLD'
}

with open('input5.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        bs1 = int(line.find(' '))
        bs2 = int(line.find(' ',bs1+1))
        bs3 = int(line.find(' ',bs2+1))
        bs4 = int(line.find(' ',bs3+1))
        bs5 = int(line.find(' ',bs4+1))
        
        num, pile1, pile2 = int(line[bs1+1:bs2]),line[bs3+1:bs4],line[bs5+1:]
        a = piles[pile1]
        b = piles[pile2]
        apendix  = a[len(a)-num:]
        print(line)
        print(piles)
        piles[pile1] = a[:len(a)-num] 
        #piles[pile2] = b + apendix[::-1] #assignment a
        piles[pile2] = b + apendix

print(piles)