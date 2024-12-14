import sys
import itertools as it

ss = []
for line in sys.stdin:
    s = line.strip()
    ss.append(s)

h = len(ss)
w = len(ss[0])
s = 0
for i,j in it.product(range(h), range(w)):
    for dx,dy in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
        if not 0 <= i+3*dy < h or not 0 <= j+3*dx < w: continue
        if ''.join([ss[i+k*dy][j+k*dx] for k in range(4)]) == 'XMAS':
            s += 1
print(s)