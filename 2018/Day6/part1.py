import sys

coords = []
for line in sys.stdin:
    x,y = map(int,line.strip().split(','))
    coords.append((x,y))

xmin,xmax = float('inf'),-float('inf')
ymin,ymax = float('inf'),-float('inf')
for x,y in coords:
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)

ctrs = {}
for xc in range(2*xmin-xmax, 2*xmax-xmin):
    for yc in range(2*ymin-ymax, 2*ymax-ymin):
        print(xc,yc,end = '\r')
        mind = float('inf')
        minj = None
        dup = False
        for j,(x,y) in enumerate(coords):
            d = abs(x-xc) + abs(y-yc)
            if d < mind:
                mind = d
                minj = j
                dup = False
            elif d == mind:
                dup = True
        if dup: continue
        if minj not in ctrs: ctrs[minj] = 0
        ctrs[minj] += 1

ctrs2 = {}
for xc in range(2*xmin-xmax-1, 2*xmax-xmin+1):
    for yc in range(2*ymin-ymax-1, 2*ymax-ymin+1):
        if 2*xmin-xmax <= xc < 2*xmax-xmin and 2*ymin-ymax <= yc < 2*ymax-ymin:
            continue
        print(xc,yc,end = '\r')
        mind = float('inf')
        minj = None
        dup = False
        for j,(x,y) in enumerate(coords):
            d = abs(x-xc) + abs(y-yc)
            if d < mind:
                mind = d
                minj = j
                dup = False
            elif d == mind:
                dup = True
        if dup: continue
        if minj not in ctrs2: ctrs2[minj] = 0
        ctrs2[minj] += 1

m = -float('inf')
for j,c in ctrs.items():
    if j in ctrs2: continue
    m = max(m,c)
print(m)