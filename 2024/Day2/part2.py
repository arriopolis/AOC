import sys

reps = []
for line in sys.stdin:
    l = list(map(int, line.strip().split()))
    reps.append(l)

s = 0
for oldr in reps:
    for j in range(len(oldr)):
        r = oldr[:j] + oldr[(j+1):]
        if not r == sorted(r) and not r == sorted(r, reverse = True): continue
        for c,d in zip(r[:-1], r[1:]):
            if abs(c-d) < 1 or abs(c-d) > 3: break
        else:
            s += 1
            break
print(s)