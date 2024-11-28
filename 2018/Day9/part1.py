import sys

pls,pts = next(sys.stdin).strip().split('; ')
n = int(pls.strip().split()[0])
pts = int(pts.strip().split()[-2])

ps = [0]
cur = 0
scores = [0]*n
player = 0
for j in range(1,pts+1):
    if j%23 == 0:
        cur -= 7
        while cur < 0: cur += len(ps)
        scores[player] += j + ps.pop(cur)
    else:
        cur += 2
        while cur > len(ps):
            cur -= len(ps)
        ps.insert(cur, j)
    player = (player+1)%n
print(max(scores))