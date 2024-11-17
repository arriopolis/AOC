import sys

origs = list(next(sys.stdin).strip())

m = float('inf')
for i in range(26):
    r = chr(ord('a')+i)
    s = [c for c in origs if c.lower() != r]
    j = 0
    while j < len(s)-1:
        c,d = s[j:j+2]
        if (c.lower() == d and d.upper() == c) or (c.upper() == d and d.lower() == c):
            del s[j+1]
            del s[j]
            j -= 1
            if j < 0: j = 0
        else:
            j += 1
    m = min(m, len(s))
print(m)