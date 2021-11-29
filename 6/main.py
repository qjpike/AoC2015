f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

field = [[0]*1000 for i in range(1000)]

for i in dat:
    if i.startswith("turn on"):
        coord1 = [int(z) for z in i.split(" ")[2].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                field[y][x] = 1
    elif i.startswith("turn off"):
        coord1 = [int(z) for z in i.split(" ")[2].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                field[y][x] = 0
    elif i.startswith("toggle"):
        coord1 = [int(z) for z in i.split(" ")[1].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                field[y][x] = (field[y][x] + 1)%2

count = 0
for i in field:
    count += i.count(1)
print("1:",count)
field = [[0]*1000 for i in range(1000)]

for i in dat:
    if i.startswith("turn on"):
        coord1 = [int(z) for z in i.split(" ")[2].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                field[y][x] += 1
    elif i.startswith("turn off"):
        coord1 = [int(z) for z in i.split(" ")[2].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                if field[y][x] > 0:
                    field[y][x] -= 1
    elif i.startswith("toggle"):
        coord1 = [int(z) for z in i.split(" ")[1].split(",")]
        coord2 = [int(z) for z in i.split(" ")[-1].split(",")]
        for y in range(coord1[1],coord2[1]+1):
            for x in range(coord1[0],coord2[0]+1):
                field[y][x] += 2

count = 0
for i in field:
    count += sum(i)

print("2:",count)