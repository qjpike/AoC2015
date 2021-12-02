inp = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSi\
ThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRn\
BFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnF\
YFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCa\
FYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'


f = open("input.txt")
dat = [i.split() for i in f.readlines()]

fd = dict()
for i in dat:
    if i[0] not in fd:
        fd[i[0]] = []
    fd[i[0]].append(i[2])

ends = set()
for i in fd:
    for j in range(0,len(inp)-len(i)+1):
        if inp[j:].startswith(i):
            for k in fd[i]:
                ends.add(inp[:j] + k + inp[j+len(i):])


print("1:",len(ends)) # 139325854187520 too high $ 419 too low


def part2(): # this is a dfs of all combinations that build from 'e' to the input value. It takes way too long to run.
    replacements = [(i[0], i[2]) for i in dat]
    replacements = sorted(replacements, key=lambda x: -len(x[-1]))

    temp = inp
    prev = 0
    while True:
        for i in replacements:
            cnt = 0
            while i[1] in temp:
                cnt += 1
                temp = temp.replace(i[1], i[0], 1)
            prev += cnt
        if temp == 'e':
            return prev

print("2:",part2())
