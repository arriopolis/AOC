import sys

s = list(next(sys.stdin).strip())
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
print(len(s))