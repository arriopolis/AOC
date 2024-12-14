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
    for dx,dy in [(-1,-1),(1,1)]:
        if not 0 <= i+2*dy < h or not 0 <= j+2*dx < w: continue
        if not ''.join([ss[i+k*dy][j+k*dx] for k in range(3)]) == 'MAS': continue
        if ''.join([ss[i+(2-k)*dy][j+k*dx] for k in range(3)]) == 'MAS' or ''.join([ss[i+k*dy][j+(2-k)*dx] for k in range(3)]) == 'MAS':
            s += 1
print(s)