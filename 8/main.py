f = open("input.txt")
dat = [i.strip() for i in f.readlines()]
hexdigits = '0123456789abcdef'
literals = 0
memory = 0
for i in dat:
    literals += len(i)
    memory += len(i) - 2
    j = 0
    while j < len(i) - 1:
        if i[j] == "\\": # if a single escape, take 1 off the length
            memory -= 1
            j += 2
            # accounting for \x## where the # digits are hex
            if i[j-1] == "x":
                if i[j] in hexdigits and i[j+1] in hexdigits:
                    memory -= 2
                    j += 2
        else:
            j += 1

print("1:",literals-memory) # 1912 is too high; 1822 too high; 1123 is too low; 1506 is wrong; 1371 is correct.
