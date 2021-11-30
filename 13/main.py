f = open("input.txt")
dat = [i.split() for i in f.readlines()]

def add_hi_to_hd(gl, amt, other, d):
    if gl == "gain":
        d[other] = amt
    else:
        d[other] = -amt

hd = dict()
for i in dat:
    if i[0] not in hd:
        hd[i[0]] = dict()
    add_hi_to_hd(i[2],int(i[3]),i[-1][:-1],hd[i[0]])

import itertools
variations = list(itertools.permutations(list(hd)))

max = 0
for i in variations:
    count = 0
    for pos,person in enumerate(i):
        count += hd[person][i[(pos + 1)%len(i)]]
        count += hd[person][i[pos - 1]]

    if count > max:
        max = count

print("1:",max)

hd["Me"] = dict()
for i in list(hd.keys()):
    if i != "Me":
        hd[i]["Me"] = 0
        hd["Me"][i] = 0


variations = list(itertools.permutations(list(hd)))
max = 0
for i in variations:
    count = 0
    for pos,person in enumerate(i):
        count += hd[person][i[(pos + 1)%len(i)]]
        count += hd[person][i[pos - 1]]

    if count > max:
        max = count

print("2:",max)