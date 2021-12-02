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
    import collections
    queue = collections.deque()
    queue.append(('e',0))
    prev = 0
    while True:
        now,cnt = queue.popleft()
        if cnt > prev:
            print(cnt)
            prev = cnt
        for i in fd:
            for j in range(0,len(now)):
                if now[j:].startswith(i):
                    for k in fd[i]:
                        new = now[:j] + k + now[j+len(i):]
                        if new == inp:
                            return cnt + 1
                        else:
                            if new not in set(queue):
                                queue.append((new,cnt+1))

print(part2())

in2 = inp.__reversed__()


