f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

dat.insert(0,'.'*len(dat[0]))
dat.append('.'*len(dat[0]))
for j,i in enumerate(dat):
    dat[j] = '.' + i + '.'
    dat[j] = list(dat[j])

import copy
dat2 = copy.deepcopy(dat)

def print_field(f):
    for i in f:
        for j in i:
            print(j,end='')
        print("")

def count_adj(coord, field):
    x,y = coord
    adj = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    count = 0
    for nx,ny in adj:
        if field[y+ny][x+nx] == "#":
            count += 1
    return count

def blinky_lights(on,off,dat):
    for x,y in on:
        dat[y][x] = "#"
    for x,y in off:
        dat[y][x] = "."

def run(cycles,dat,always_on=[]):
    for i in range(cycles):
        turn_on = []
        turn_off = []
        for y in range(1,len(dat)-1,1):
            for x in range(1,len(dat[0])-1,1):
                c = count_adj((x,y),dat)
                if dat[y][x] == "#" and c not in [2,3]:
                    turn_off.append((x,y))
                elif dat[y][x] == "." and c == 3:
                    turn_on.append((x,y))

        blinky_lights(turn_on, turn_off, dat)
        blinky_lights(always_on,[],dat)
        # print_field(dat)
        # print("-------------------------------------------------------------------------------------------------------------------")

run(100,dat)
count = sum([i.count("#") for i in dat])
print("1:",count)

always_on = [(1,1),(len(dat2) - 2,1),(1,len(dat2) - 2),(len(dat2) - 2,len(dat2) - 2)]
blinky_lights(always_on,[],dat2)

print_field(dat2)
run(100,dat2,always_on)
count = sum([i.count("#") for i in dat2])
print("2:",count) 
