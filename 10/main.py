inp = '1321131112'


for i in range(40):
    ptr = 0
    outp = ''
    while ptr < len(inp):
        count = 1
        while ptr + count < len(inp) and inp[ptr+count] == inp[ptr]:
            count += 1

        outp += str(count) + inp[ptr]
        ptr += count
    inp = outp

print("1:",len(outp))

inp = '1321131112'

for i in range(50):# part 2 takes a while
    ptr = 0
    outp = ''
    while ptr < len(inp):
        count = 1
        while ptr + count < len(inp) and inp[ptr+count] == inp[ptr]:
            count += 1

        outp += str(count) + inp[ptr]
        ptr += count
    inp = outp

print("2:",len(outp))