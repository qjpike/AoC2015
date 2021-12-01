f = open("input.txt")
dat = [i.split() for i in f.readlines()]

rb = dict()
for i in dat:
    rb[i[0]] = [int(i[2][:-1]), int(i[4][:-1]), int(i[6][:-1]),int(i[8][:-1]), int(i[10])]



max = 0
max2 = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            h = 100-k-j-i
            if h >= 0:
                cap = rb["Sprinkles:"][0]*i + rb["PeanutButter:"][0]*j + rb["Frosting:"][0]*k + rb["Sugar:"][0]*h
                dur = rb["Sprinkles:"][1]*i + rb["PeanutButter:"][1]*j + rb["Frosting:"][1]*k + rb["Sugar:"][1]*h
                fla = rb["Sprinkles:"][2]*i + rb["PeanutButter:"][2]*j + rb["Frosting:"][2]*k + rb["Sugar:"][2]*h
                tex = rb["Sprinkles:"][3]*i + rb["PeanutButter:"][3]*j + rb["Frosting:"][3]*k + rb["Sugar:"][3]*h
                cal = rb["Sprinkles:"][4]*i + rb["PeanutButter:"][4]*j + rb["Frosting:"][4]*k + rb["Sugar:"][4]*h

                prod = 1
                prod *= cap if cap > 0 else 1
                prod *= dur if dur > 0 else 1
                prod *= fla if fla > 0 else 1
                prod *= tex if tex > 0 else 1


            if prod > max:
                max = prod

            if cal == 500 and prod > max2:
                max2 = prod


print("1:",max)
print("2:",max2)