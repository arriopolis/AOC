import sys

ll,lr = [],[]
for line in sys.stdin:
    a,b = map(int,line.strip().split())
    ll.append(a)
    lr.append(b)

ll.sort()
lr.sort()

print(sum(abs(b-a) for a,b in zip(ll,lr)))