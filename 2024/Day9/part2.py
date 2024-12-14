import sys

line = next(sys.stdin).strip()

pos = 0
blocks = []
for b,f in zip(line[::2],line[1::2]):
    b,f = map(int, (b,f))
    blocks.append((b, pos,len(blocks)))
    pos += b + f
if len(line)%2 == 1: blocks.append((int(line[-1]),pos,len(blocks)))

orig_blocks = set(blocks)
tot = 0
while True:
    for j2,(b,s,idx) in reversed(list(enumerate(blocks))):
        if (b,s,idx) not in orig_blocks: continue
        orig_blocks.remove((b,s,idx))
        for j,((b1,s1,_),(b2,s2,_)) in enumerate(zip(blocks[:-1],blocks[1:])):
            if j >= j2: break
            if s2-(s1+b1) >= b:
                blocks.insert(j+1,(b,s1+b1,idx))
                blocks.remove((b,s,idx))
                break
        else: continue
        break
    else: break

tot = 0
for b,s,idx in blocks:
    for pos in range(s,s+b):
        tot += pos*idx
print(tot)