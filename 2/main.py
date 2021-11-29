f = open("input.txt")
dat = [i.split("x") for i in f.readlines()]

need = 0
ribbon = 0
for i in dat:
    s1 = int(i[0])*int(i[1])
    s2 = int(i[1])*int(i[2])
    s3 = int(i[2])*int(i[0])
    arr = [s1,s2,s3]
    arr.sort()
    need += arr[0]*3 + arr[1]*2 + arr[2]*2

    arr2 = [int(i[0]),int(i[1]),int(i[2])]
    arr2.sort()
    ribbon += arr2[0]*2 + arr2[1]*2 + arr2[0]*arr2[1]*arr2[2]


print("1:",need)
print("2:",ribbon)