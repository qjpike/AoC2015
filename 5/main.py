f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

def count_vowels(str):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in str:
        if i in vowels:
            count += 1
            if count == 3:
                return True
    return False

def find_double_letters(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return True
    return False

def find_unallowed(str):
    unallowed = ["ab","cd","pq","xy"]
    for i in unallowed:
        if i in str:
            return True
    return False

def find_repeat_doubles(s):
    for i in range(len(s)):
        if s[i:i+2] in s[i+2:]:
            return True
    return False

def find_skip(str):
    for i in range(len(str)-2):
        if str[i] == str[i+2]:
            return True
    return False


nice_list = 0
nice_list_2 = 0
for i in dat:
    if count_vowels(i) and find_double_letters(i) and not find_unallowed(i):
        nice_list += 1

    if find_skip(i) and find_repeat_doubles(i):
        nice_list_2 += 1


print("1:",nice_list)
print("2:",nice_list_2) # 67 is wrong