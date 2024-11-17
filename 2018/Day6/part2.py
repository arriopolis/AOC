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

ctr = 0
for xc in range(2*xmin-xmax, 2*xmax-xmin):
    for yc in range(2*ymin-ymax, 2*ymax-ymin):
        d = 0
        for x,y in coords:
            d += abs(x-xc) + abs(y-yc)
        if d < 10000:
            ctr += 1
print(ctr)