import sys

line = next(sys.stdin).strip()

pos = 0
blocks = []
for b,f in zip(line[::2],line[1::2]):
    b,f = map(int, (b,f))
    blocks.append((b, pos))
    pos += b + f
if len(line)%2 == 1: blocks.append((int(line[-1]),pos))

tot = 0
for j,(b,s) in enumerate(blocks):
    for pos in range(s,s+b):
        tot += pos * j
    
    if len(blocks) == j+1: break
    _,news = blocks[j+1]
    for pos in range(s+b,news):
        lastb,lasts = blocks[-1]
        lastj = len(blocks)-1
        tot += pos * lastj
        if lastb == 1:
            blocks.pop()
            if len(blocks) == j+1: break
        else:
            blocks[-1] = (lastb-1,lasts)
    if len(blocks) == j+1: break
print(tot)