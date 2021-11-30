import collections

f = open("input.txt")
dat = [i.split() for i in f.readlines()]

# using a dict of sets of tuples to prevent duplications
routes = dict()
for i in dat:
    if i[0] not in routes:
        routes[i[0]] = set()
        routes[i[0]].add((i[0],0))
    routes[i[0]].add((i[2],int(i[-1])))

    if i[2] not in routes:
        routes[i[2]] = set()
        routes[i[2]].add((i[2],0))

    routes[i[2]].add((i[0],int(i[-1])))

locs = sorted(list(routes.keys()))

matrix = []
for i in locs:
    arr = list(routes[i])
    arr.sort()
    matrix.append(arr)

import itertools

t = list(itertools.permutations(range(8)))
min = 9999999999
max = 0
for i in t:
    cur = i[0]
    dist = 0
    for j in i[1:]:
        dist += matrix[cur][j][1]
        cur = j
    if dist < min:
        min = dist
    if dist > max:
        max = dist

print("1:",min)
print("2:",max)
