start = 'hxbxxyzz'

def increasing_str(a):
    for i in range(len(a) - 2):
        if ord(a[i+1]) == ord(a[i]) + 1 and ord(a[i+2]) == ord(a[i]) + 2:
            return True
    return False

def contains_bad(a):
    bad = ['i','o','l']
    for i in bad:
        if i in a:
            return True
    return False

def contains_pairs(a):
    count = 0
    ptr = 0
    while ptr < len(a) - 1:
        if a[ptr] == a[ptr+1]:
            count += 1
            ptr += 1
        ptr += 1
    return count >= 2

def increment_str(a):
    l = list(a)
    curr = -1
    if ord(l[curr]) < ord('z'):
        l[curr] = chr(ord(l[curr]) + 1)
    else:
        return increment_str(''.join(l[:-1])) + 'a'
    return ''.join(l)

def find_next(inp):
    while True:
        if not contains_bad(inp):
            if increasing_str(inp):
                if contains_pairs(inp):
                    break
        inp = increment_str(inp)
    return inp

first = find_next(start)
print("1:",first)
first = increment_str(first)
print("2:",find_next(first))
