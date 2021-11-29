f = open("input.txt")
dat = f.read().strip()

up = dat.count("(")
down = dat.count(")")

print("1:", up - down)

floor = 0
for i in range(len(dat)):
    if dat[i] == "(":
        floor += 1
    elif dat[i] == ")":
        floor -= 1
        if floor < 0:
            print("2:",i+1)
            break