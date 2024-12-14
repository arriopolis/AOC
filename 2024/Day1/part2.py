import sys

ll,lr = [],[]
for line in sys.stdin:
    a,b = map(int,line.strip().split())
    ll.append(a)
    lr.append(b)

lr_occ = {}
for x in lr:
    if x not in lr_occ: lr_occ[x] = 0
    lr_occ[x] += 1

s = 0
for a in ll:
    if a in lr_occ:
        s += a*lr_occ[a]
print(s)