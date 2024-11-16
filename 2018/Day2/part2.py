import sys
import itertools as it

words = set()
for line in sys.stdin:
    words.add(line.strip())

for w1,w2 in it.combinations(words, 2):
    diff = sum(1 if c != d else 0 for c,d in zip(w1,w2))
    if diff == 1:
        print(''.join(c for c,d in zip(w1,w2) if c == d))
        sys.exit()