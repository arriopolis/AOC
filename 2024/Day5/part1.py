import sys

ss = []
for line in sys.stdin:
    ss.append(line.strip())

rules = set()
for j,s in enumerate(ss):
    if not s: break
    a,b = map(int,s.split('|'))
    rules.add((a,b))

tot = 0
for s in ss[j+1:]:
    l = list(map(int,s.split(',')))
    for c,d in zip(l[:-1],l[1:]):
        if (d,c) in rules:
            break
    else:
        tot += l[len(l)//2]
print(tot)