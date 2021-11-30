f = open("input.txt")
dat = f.read().strip()
f.close()
import re

reg = re.compile('[-0-9]+')

res = reg.findall(dat)

count = 0
for i in res:
    count += int(i)

print("1:",count) #22716 is too low ; 203051 is too high

og_count = count
import json
t = json.loads(dat)

def find_sum(s):
    reg = re.compile('[-0-9]+')
    res = reg.findall(s)
    count = 0
    for i in res:
        count += int(i)
    return count

def rec_find(a):
    count = 0
    if isinstance(a,dict):
        output = {}
        if "red" not in a.values():
            for k,v in a.items():
                output[k] = rec_find(v)
    elif isinstance(a,list):
        output = []
        for v in a:
            output.append(rec_find(v))
    else:
        output = a
    return output


t = rec_find(t)
print("2:",find_sum(json.dumps(t))) # 122688 is too high;
