import collections
import random
f = open("input.txt")
dat = collections.deque([i.split() for i in f.readlines()])

wires = dict()

while len(dat) > 0:
    i = dat.popleft()

    if len(i) == 3:
        if i[0].isnumeric():
            wires[i[2]] = int(i[0])
        elif i[0] not in wires:
            dat.append(i)
        else:
            wires[i[2]] = wires[i[0]]

    elif len(i) == 4:
        if i[1] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[1]] ^ 65535
    elif i[1] == "AND":
        if i[0].isnumeric() and i[2] in wires:
            wires[i[-1]] = int(i[0]) & wires[i[2]]
        elif i[0] not in wires or i[2] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] & wires[i[2]]
    elif i[1] == "OR":
        if i[0] not in wires or i[2] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] | wires[i[2]]
    elif i[1] == "RSHIFT":
        if i[0] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] >> int(i[2])
    elif i[1] == "LSHIFT":
        if i[0] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] << int(i[2])


res = wires['a']
print("1:",res)
f.close()
f = open("input.txt")
dat = collections.deque([i.split() for i in f.readlines()])

wires = dict()
wires['b'] = res

while len(dat) > 0:
    i = dat.popleft()
    if i[0] == '14146': # wire b already assigned above. throw away that entry.
        i = dat.popleft()
    if len(i) == 3:
        if i[0].isnumeric():
            wires[i[2]] = int(i[0])
        elif i[0] not in wires:
            dat.append(i)
        else:
            wires[i[2]] = wires[i[0]]

    elif len(i) == 4:
        if i[1] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[1]] ^ 65535
    elif i[1] == "AND":
        if i[0].isnumeric() and i[2] in wires:
            wires[i[-1]] = int(i[0]) & wires[i[2]]
        elif i[0] not in wires or i[2] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] & wires[i[2]]
    elif i[1] == "OR":
        if i[0] not in wires or i[2] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] | wires[i[2]]
    elif i[1] == "RSHIFT":
        if i[0] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] >> int(i[2])
    elif i[1] == "LSHIFT":
        if i[0] not in wires:
            dat.append(i)
        else:
            wires[i[-1]] = wires[i[0]] << int(i[2])


    for i in wires.values():
        if i > 65535:
            print("Too Big!")

print("2:",wires['a']) # 33706 is wrong