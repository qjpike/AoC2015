inp = 'ckczppom'

import hashlib

found_5 = False
found_6 = False
for i in range(10000000000):
    if hashlib.md5((inp+str(i)).encode()).hexdigest()[:5] == '00000' and not found_5:
        print("1:",i)
        found_5 = True
    if hashlib.md5((inp+str(i)).encode()).hexdigest()[:6] == '000000' and not found_6:
        print("2:",i)
        found_6 = True

    if found_6 and found_5:
        break