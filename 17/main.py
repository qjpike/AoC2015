f = open("input.txt")
buckets = [int(i) for i in f.readlines()]

target = 150
import itertools

count = 0
for i in range(len(buckets)):
    for seq in itertools.combinations(buckets, i):
        if sum(seq) == target:
            count += 1

print("1:", count)

seq = []
min = 99
for i in range(len(buckets)):
    for way in itertools.combinations(buckets,i):
        if sum(way) == target:
            if len(way) < min:
                min = len(way)
                seq = [way]
            elif len(way) == min:
                seq.append(min)



print("2:",len(seq)) # 18 is wrong