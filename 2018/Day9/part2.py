import sys

pls,pts = next(sys.stdin).strip().split('; ')
n = int(pls.strip().split()[0])
pts = int(pts.strip().split()[-2])*100

ps = [(0,0,0)]
cur = 0
scores = [0]*n
player = 0
for j in range(1,pts+1):
    print(j, '/', pts+1, end = '\r')
    if j%23 == 0:
        # Move 7 steps to the left
        for _ in range(7):
            cur = ps[cur][1]
        
        # Remove the current element
        v,l,r = ps[cur]
        v1,l1,r1 = ps[l]
        v2,l2,r2 = ps[r]
        ps[l] = (v1,l1,r)
        ps[r] = (v2,l,r2)
        cur = r

        # Add to the score
        scores[player] += j + v
    else:
        # Move to the right
        cur = ps[cur][2]
        
        # Insert right
        v1,l1,r1 = ps[cur]
        v2,l2,r2 = ps[r1]
        idx = len(ps)
        ps.append((j,cur,r1))
        ps[r1] = (v2,idx,r2)
        ps[cur] = (v1,l1,idx)
        cur = idx
    player = (player+1)%n

print()
print(max(scores))