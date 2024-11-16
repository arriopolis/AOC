import sys

num2,num3 = 0,0
for line in sys.stdin:
    s = line.strip()
    d = {}
    for c in s:
        if c not in d: d[c] = 0
        d[c] += 1

    nums = set(d.values())
    if 2 in nums: num2 += 1
    if 3 in nums: num3 += 1
print(num2 * num3)