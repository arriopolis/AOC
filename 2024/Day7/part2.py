import sys
import itertools as it

eqs = []
for line in sys.stdin:
    res, ns = line.strip().split(': ')
    eqs.append((int(res), list(map(int, ns.strip().split()))))

tot = 0
for res,ns in eqs:
    for ops in it.product('+*|', repeat = len(ns)-1):
        newres = ns[0]
        for j in range(1,len(ns)):
            if ops[j-1] == '+': newres += ns[j]
            elif ops[j-1] == '*': newres *= ns[j]
            elif ops[j-1] == '|': newres = int(str(newres) + str(ns[j]))
            if newres > res: break
        if newres == res:
            tot += res
            break
print(tot)