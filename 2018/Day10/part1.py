import sys

ps = []
for line in sys.stdin:
    p,v = line.strip().split(' velocity=')
    x,y = map(int,p.strip().rstrip('>').split('<')[1].split(', '))
    vx,vy = map(int,v.strip().rstrip('>').split('<')[1].split(', '))
    ps.append((x,y,vx,vy))

j = 10918

def compute_area(j):
    s = set()
    xmin,xmax,ymin,ymax = float('inf'),-float('inf'),float('inf'),-float('inf')
    for x,y,vx,vy in ps:
        newx,newy = x+j*vx,y+j*vy
        s.add((newx,newy))
        xmin = min(xmin,newx)
        xmax = max(xmax,newx)
        ymin = min(ymin,newy)
        ymax = max(ymax,newy)
    return s,xmin,xmax,ymin,ymax

min_area = float('inf')
min_j = None
for j in range(20000):
    print(j, '/', 20000, end = '\r')
    s,xmin,xmax,ymin,ymax = compute_area(j)
    area = (xmax - xmin)*(ymax-ymin)
    if area < min_area:
        min_area = area
        min_j = j
print()

s,xmin,xmax,ymin,ymax = compute_area(min_j)

for y in range(ymin,ymax+1):
    for x in range(xmin,xmax+1):
        if (x,y) in s:
            print('#', end = ' ')
        else:
            print('.', end = ' ')
    print()