import sys

Gf = {}
Gb = {}
for line in sys.stdin:
    l = line.strip().split()
    u = l[1]
    v = l[7]
    if u not in Gf: Gf[u] = set()
    if v not in Gf: Gf[v] = set()
    Gf[u].add(v)

    if u not in Gb: Gb[u] = set()
    if v not in Gb: Gb[v] = set()
    Gb[v].add(u)

res = []
while Gb:
    u = min(Gb.keys(), key = lambda x : (len(Gb[x]),x))
    res.append(u)
    del Gb[u]
    for v in Gf[u]:
        Gb[v].remove(u)
    del Gf[u]
print(''.join(res))