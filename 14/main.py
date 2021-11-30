f = open("input.txt")
dat = [i.split() for i in f.readlines()]

class Reindeer:

    def __init__(self, name, speed, duration, rest):
        self.pos = 0
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.state = 'fly'
        self.state_counter = 0
        self.points = 0

    def add_point(self):
        self.points += 1

    def move(self):
        if self.state == 'fly':
            self.pos += self.speed
            self.state_counter += 1
            if self.state_counter == self.duration:
                self.state_counter = 0
                self.state = 'rest'
        else:
            self.state_counter += 1
            if self.state_counter == self.rest:
                self.state_counter = 0
                self.state = 'fly'

deer = []
for i in dat:
    deer.append(Reindeer(i[0], int(i[3]), int(i[6]), int(i[-2])))

for i in range(2503):
    for j in deer:
        j.move()
    max = 0
    pos = -1
    for d,j in enumerate(deer):
        if j.pos > max:
            max = j.pos
            pos = [d]
        elif j.pos == max:
            pos.append(d)
    for d in pos:
        deer[d].add_point()

max_final = 0
points_final = 0
for i in deer:
    if i.pos > max_final:
        max_final = i.pos
    if i.points > points_final:
        points_final = i.points

print("1:",max_final)
print("2:",points_final) #1064 too low #1065 too low #2166 too high #2167 wrong

