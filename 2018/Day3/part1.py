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

intsns = list(set(find_intsns(rects).values()))

todel = set()
for (i,rect1),(j,rect2) in it.permutations(enumerate(intsns), 2):
    x1,y1,w1,h1 = rect1
    x2,y2,w2,h2 = rect2
    if not (x1 <= x2 < x2+w2 <= x1+w1): continue
    if not (y1 <= y2 < y2+h2 <= y1+h1): continue
    todel.add(j)
for j in sorted(todel, reverse = True):
    del intsns[j]

def compute_area(rects):
    A = 0
    intsns = {rect : [tuple([j])] for j, rect in enumerate(rects)}
    for j in range(1,len(rects)+1):
        print(j, len(intsns), ' '*50)
        t = 0
        for rect,ss in intsns.items():
            assert all(len(s) == j for s in ss)
            assert all(tuple(sorted(s)) == s for s in ss)
            _,_,w,h = rect
            t += w*h * len(ss)
        A += (-1)**(j+1) * t
        
        n = len(intsns)
        new_intsns = {}
        for i,(rect,ss) in enumerate(intsns.items()):
            print(i, '/', n, ':', len(ss), ' '*50, end = '\r')
            Omega = set.union(*map(set,ss))
            newl = set()
            for s in ss:
                for k in Omega.difference(s):
                    newl.add(tuple(sorted(set(s).union([k]))))
            if newl:
                new_intsns[rect] = newl
        
        for i,((rect1,ss1),(rect2,ss2)) in enumerate(it.combinations(intsns.items(), 2)):
            print(i, '/', n*(n-1)//2, ':', len(ss1), len(ss2), end = '\r')
            x1,y1,w1,h1 = rect1
            x2,y2,w2,h2 = rect2
            xmin = max(x1,x2)
            xmax = min(x1+w1,x2+w2)
            ymin = max(y1,y2)
            ymax = min(y1+h1,y2+h2)
            if xmin >= xmax: continue
            if ymin >= ymax: continue

            rect = (xmin,ymin,xmax-xmin,ymax-ymin)
            newl = set() if rect not in new_intsns else new_intsns[rect]
            
            sdict1 = {}
            for s1 in ss1:
                for k in s1:
                    s = tuple(sorted(set(s1).difference([k])))
                    if s not in sdict1: sdict1[s] = set()
                    sdict1[s].add(k)
            
            sdict2 = {}
            for s2 in ss2:
                for k in s2:
                    s = tuple(sorted(set(s2).difference([k])))
                    if s not in sdict2: sdict2[s] = set()
                    sdict2[s].add(k)
            
            for s in sdict1:
                if s not in sdict2: continue
                for k1,k2 in it.product(sdict1[s], sdict2[s]):
                    if k1 != k2:
                        news = set(s).union([k1,k2])
                        newl.add(tuple(sorted(news)))
            
            if newl:
                new_intsns[rect] = newl
        
        intsns = new_intsns
        if not intsns: break
    
    return A

A = compute_area(intsns)
print()
print(A)