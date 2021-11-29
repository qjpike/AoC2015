f = open("input.txt")
dat = f.read().strip()

houses = dict()
moves = ["^",">","v","<"]
moves_coord = [(0,1),(1,0),(0,-1),(-1,0)]

pos = (0,0)
houses[pos] = 1
for i in dat:
    if (pos[0] + moves_coord[moves.index(i)][0], pos[1] + moves_coord[moves.index(i)][1]) not in houses:
        houses[(pos[0] + moves_coord[moves.index(i)][0], pos[1] + moves_coord[moves.index(i)][1])] = 1
    else:
        houses[(pos[0] + moves_coord[moves.index(i)][0], pos[1] + moves_coord[moves.index(i)][1])] += 1

    pos = (pos[0] + moves_coord[moves.index(i)][0], pos[1] + moves_coord[moves.index(i)][1])

print("1:",houses.keys().__len__())

houses = dict()

s_pos = (0,0)
r_pos = (0,0)
for i in range(0,len(dat),2):
    if (s_pos[0] + moves_coord[moves.index(dat[i])][0], s_pos[1] + moves_coord[moves.index(dat[i])][1]) not in houses:
        houses[(s_pos[0] + moves_coord[moves.index(dat[i])][0], s_pos[1] + moves_coord[moves.index(dat[i])][1])] = 1
    else:
        houses[(s_pos[0] + moves_coord[moves.index(dat[i])][0], s_pos[1] + moves_coord[moves.index(dat[i])][1])] += 1
    s_pos = (s_pos[0] + moves_coord[moves.index(dat[i])][0], s_pos[1] + moves_coord[moves.index(dat[i])][1])

    if (r_pos[0] + moves_coord[moves.index(dat[i+1])][0], r_pos[1] + moves_coord[moves.index(dat[i+1])][1]) not in houses:
        houses[(r_pos[0] + moves_coord[moves.index(dat[i+1])][0], r_pos[1] + moves_coord[moves.index(dat[i+1])][1])] = 1
    else:
        houses[(r_pos[0] + moves_coord[moves.index(dat[i+1])][0], r_pos[1] + moves_coord[moves.index(dat[i+1])][1])] += 1
    r_pos = (r_pos[0] + moves_coord[moves.index(dat[i+1])][0], r_pos[1] + moves_coord[moves.index(dat[i+1])][1])


print("2:",houses.keys().__len__())