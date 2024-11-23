import sys

l = list(map(int,next(sys.stdin).strip().split()))

def read_node(revl):
    num_children = revl.pop()
    num_entries = revl.pop()

    children = []
    for _ in range(num_children):
        children.append(read_node(revl))
    
    entries = [revl.pop() for _ in range(num_entries)]

    return children, entries

tree = read_node(list(reversed(l)))

def compute_value(tree):
    children, entries = tree

    if not children:
        return sum(entries)
    
    values = [compute_value(c) for c in children]
    t = 0
    for j in entries:
        if not 1 <= j <= len(values): continue
        t += values[j-1]
    return t

print(compute_value(tree))