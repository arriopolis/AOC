import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

s = ''.join(lines)

tot = 0
res = -1
while True:
    res = s.find('mul(', res+1)
    if res == -1: break
    res2 = s.find(',', res+4)
    if res2 == -1: break
    res3 = s.find(')', res2+1)
    if res3 == -1: break
    
    int1 = s[res+4:res2]
    int2 = s[res2+1:res3]
    if any(c not in '0123456789' for c in int1): continue
    if any(c not in '0123456789' for c in int2): continue
    tot += int(int1) * int(int2)

print(tot)