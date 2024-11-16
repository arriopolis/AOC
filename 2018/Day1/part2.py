import sys

nums = []
for line in sys.stdin:
    line = line.strip()
    m = -1 if line[0] == '-' else 1
    nums.append(m*int(line[1:]))
    
visited = set([0])
s = 0
while True:
    for n in nums:
        s += n
        if s in visited:
            print(s)
            sys.exit()
        visited.add(s)