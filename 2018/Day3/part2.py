import sys
import itertools as it

rects = []
for line in sys.stdin:
    data = line.strip().split('@')[1].strip()
    pos,size = data.split(': ')
    x,y = map(int,pos.split(','))
    w,h = map(int,size.split('x'))
    rects.append((x,y,w,h))

def find_intsns(rects):
    intsns = {}
    for (i,rect1),(j,rect2) in it.combinations(enumerate(rects), 2):
        x1,y1,w1,h1 = rect1
        x2,y2,w2,h2 = rect2
        xmin = max(x1,x2)
        xmax = min(x1+w1,x2+w2)
        ymin = max(y1,y2)
        ymax = min(y1+h1,y2+h2)
        if xmin >= xmax: continue
        if ymin >= ymax: continue
        intsn = (xmin,ymin,xmax-xmin,ymax-ymin)
        intsns[tuple(sorted([i,j]))] = intsn
    return intsns

intsns = set.union(*map(set,find_intsns(rects).keys()))
print(list(set(range(len(rects))).difference(intsns))[0] + 1)