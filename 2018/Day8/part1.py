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

def sum_entries(tree):
    children, entries = tree
    t = sum(entries)
    for c in children:
        t += sum_entries(c)
    return t

print(sum_entries(tree))