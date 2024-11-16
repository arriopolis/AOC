import sys

s = 0
for line in sys.stdin:
    line = line.strip()
    m = -1 if line[0] == '-' else 1
    s += m*int(line[1:])
print(s)