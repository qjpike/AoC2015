f = open("input.txt")
dat = [i.split() for i in f.readlines()]

sd = dict()
for i in dat:
    sd[i[1][:-1]] = dict()
    for k in range(2,len(i),2):
        sd[i[1][:-1]][i[k][:-1]] = int(i[k+1].split(",")[0])

sender = [('children', 3),('cats', 7),('samoyeds', 2),
          ('pomeranians', 3),('akitas', 0),('vizslas', 0),
          ('goldfish', 5),('trees', 3),('cars', 2),('perfumes', 1)]

most = 0
sue = -1
for i in sd:
    num = 0
    for attr,amt in sender:
        if attr in sd[i] and sd[i][attr] == amt:
            num += 1

    if num > most:
        sue = i
        most = num

print("1:",sue)

most = 0
sue = -1
for i in sd:
    num = 0
    for attr,amt in sender:
        if attr in sd[i]:
            if attr == 'cats' and sd[i][attr] > amt:
                num += 1
            elif attr == 'cats' and sd[i][attr] > amt:
                num += 1
            elif attr == 'pomeranians' and sd[i][attr] < amt:
                num += 1
            elif attr == 'goldfish' and sd[i][attr] < amt:
                num += 1
            elif sd[i][attr] == amt:
                num += 1

    if num > most:
        most = num
        sue = i

print("2:",sue) # 232 is too low